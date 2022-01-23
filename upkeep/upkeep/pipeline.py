import os
import re
import logging
import pandas as pd
from pandas.core.frame import DataFrame
from dotenv import load_dotenv
load_dotenv('../.env')

from . import constants, schema, db

LOGGER = logging.getLogger(__name__)
ENGINE = db.get_engine()
CHUNK_SIZE = int(os.environ.get('CHUNK_SIZE', '50000'))


def collect_data():
    chunks = []
    with pd.read_csv(
        constants.DATA_FILE_URL,
        delimiter=',',
        decimal='.',
        dtype={'RegionName': str, 'RegionCode': str},
        usecols=constants.OXFORD_FILE_COLUMNS,
        chunksize=CHUNK_SIZE
    ) as reader:
        for i, chunk in enumerate(reader):
            LOGGER.info(f"Progress: {str(CHUNK_SIZE * (i + 1))} lines read")
            chunks.append(chunk)
    return pd.concat(chunks, ignore_index=True)


def map_column_name(name):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return re.sub('[^0-9a-zA-Z]+', '_', snake_case).strip('_')


def get_region_id_and_name(row):
    region_id = row['region_code'] if row['jurisdiction'] == 'STATE_TOTAL' else row['country_code']
    region_name = row['region_name'] if row['jurisdiction'] == 'STATE_TOTAL' else row['country_name']
    return region_id, region_name  


def process(data: DataFrame):
    data = data.rename(columns=map_column_name)
    data.loc[:, 'region_id'], data.loc[:, 'region_name'] = zip(*data.apply(get_region_id_and_name, axis=1))
    data['date'] = pd.to_datetime(data['date'].astype(str))
    data.loc[:, constants.INPUT_COLUMNS] = data.loc[:, constants.INPUT_COLUMNS].fillna(0)
    data = data.query(" & ".join([f"{column} < 10" for column in constants.INPUT_COLUMNS]))
    return data


def get_region_table(data: DataFrame):
    region_data = data[['region_id', 'region_name', 'jurisdiction']].rename(
        columns={'region_id': 'id', 'region_name': 'name', 'jurisdiction': 'type'})
    region_data = region_data.groupby('id').first().reset_index()
    region_data.loc[:, 'type'] = region_data.loc[:, 'type'].apply(lambda x: x.split('_')[0])
    return region_data


def get_covid_full_table(data: DataFrame):
    covid_full = data.drop(columns=['country_name', 'country_code', 'region_name', 'region_code', 'jurisdiction'])
    region_id_col = covid_full.pop("region_id")
    covid_full.insert(0, region_id_col.name, region_id_col)
    return covid_full


def publish_table(name: str, table: DataFrame, **kwargs):
    LOGGER.info(f"Publishing table {name}")
    table.to_sql(name=name, con=ENGINE, if_exists='replace', index=False, **kwargs)


def pipeline():
    """Updates the database with the latest data from the oxford dataset.
    Returns the updated tables.
    """
    LOGGER.info('Collecting data')
    data = collect_data()
    LOGGER.info('Processing data')
    processed_data = process(data)
    region = get_region_table(processed_data)
    covid_full = get_covid_full_table(processed_data)
    publish_table('region', region, dtype=schema.region)
    publish_table('covid_full', covid_full, dtype=schema.covid_full)
    return region, covid_full
