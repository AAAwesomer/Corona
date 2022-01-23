import lightgbm as lgb
import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from . import constants

assert not constants.N_PREDICTION_DAYS % constants.N_BUCKETS, (
    "# of buckets does not divide # of prediction days"
)

COL_REGION = "region_id"
COL_PREDICTION = "prediction"
COL_CASES = "confirmed_cases"
COL_WINDOW = "prediction_window"


def get_buckets():
    bucket_size = constants.N_PREDICTION_DAYS // constants.N_BUCKETS
    return [(i * bucket_size, bucket_size * (i + 1) - 1)
            for i in range(constants.N_BUCKETS)]


def get_cases_column_names():
    return ["confirmed_cases_{}_days_ago".format(constants.N_INPUT_DAYS - 1 - i)
            for i in range(constants.N_INPUT_DAYS - 1)]


def random_from_tuple(t):
    return random.randint(t[0], t[1])


def get_rolling_values(df, column, window):
    return np.lib.stride_tricks.as_strided(df[column],
                                           (len(df) - (window - 1), window),
                                           (df[column].values.strides * 2))

def add_cases_columns(inputdf, window=constants.N_INPUT_DAYS):
    arrays = get_rolling_values(inputdf, COL_CASES, window)
    inputdf.reset_index(inplace=True, drop=True)
    inputdf.loc[window - 1:, get_cases_column_names() + [COL_CASES]] = arrays
    return inputdf


def cases_columns_to_percentages(inputdf):
    cases_columns = get_cases_column_names() + [COL_PREDICTION]
    for cases_column in cases_columns:
        inputdf.loc[:, cases_column] = inputdf.loc[:, cases_column] / inputdf.loc[:, COL_CASES]
        inputdf.loc[:, cases_column] = inputdf.loc[:, cases_column].shift(1)
    return inputdf


def add_prediction_rows(inputdf, window=constants.N_PREDICTION_DAYS):
    arrays = get_rolling_values(inputdf, COL_CASES, window)
    inputdf.reset_index(inplace=True, drop=True)
    inputdf.loc[window - 1:, COL_PREDICTION] = pd.Series(list(arrays))
    inputdf.loc[:, COL_PREDICTION] = inputdf \
        .groupby(COL_REGION)[COL_PREDICTION] \
        .transform(lambda x: x.shift(-1))
    inputdf = cases_columns_to_percentages(inputdf)
    inputdf.dropna(inplace=True)
    inputdf[COL_PREDICTION] = inputdf[COL_PREDICTION] \
        .apply(lambda x: [[i, n] for i, n in enumerate(x)])
    sampled_dates = [random_from_tuple(bucket) for bucket in get_buckets()]
    inputdf[COL_PREDICTION] = inputdf[COL_PREDICTION] \
        .apply(lambda x: [x[date] for date in sampled_dates])
    inputdf = inputdf.explode(COL_PREDICTION).iloc[window:]
    inputdf[COL_WINDOW] = inputdf[COL_PREDICTION].apply(lambda x: x[0] + 1)
    inputdf[COL_PREDICTION] = inputdf[COL_PREDICTION].apply(lambda x: x[1])
    return inputdf.drop(columns=[COL_CASES])


def preprocess_confirmed_cases_input(data):
    inputdf = data[data[COL_CASES] > 1000]
    inputdf.loc[:, constants.FLAG_COLUMNS] = inputdf \
        .loc[:, constants.FLAG_COLUMNS].fillna(1)
    inputdf.loc[:, constants.INPUT_COLUMNS] = inputdf \
        .groupby(COL_REGION)[constants.INPUT_COLUMNS] \
        .transform(lambda x: x.ffill())
    inputdf = add_cases_columns(inputdf)
    inputdf = add_prediction_rows(inputdf)
    return inputdf.dropna().reset_index(drop=True)


def x_y(input):
    X = input[constants.INPUT_COLUMNS + get_cases_column_names() + [COL_WINDOW]]
    y = input[COL_PREDICTION]
    return X, y


def prepare_train_data(input):
    return lgb.Dataset(*x_y(input))


def prepare_train_and_eval(input):
    X_train, X_test, y_train, y_test = train_test_split(
        *x_y(input), test_size = 0.2, random_state=42, shuffle=False)
    print(X_test)
    lgb_train = lgb.Dataset(X_train, y_train)
    lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)
    return lgb_train, lgb_eval


def load_train_data(filename):
    return lgb.Dataset(filename)


def train_model(train_data: lgb.Dataset, params=None, eval_data=None,
                num_boost_round=constants.MODEL_NUM_ROUNDS):
    params = params or constants.MODEL_PARAMS
    callbacks = [lgb.early_stopping(stopping_rounds=200)] if eval_data else None
    return lgb.train(params,
                     train_data,
                     num_boost_round=num_boost_round,
                     valid_sets=eval_data,
                     callbacks=callbacks)


def train(data):
    confirmed_cases_input = preprocess_confirmed_cases_input(data)
    train_data = prepare_train_data(confirmed_cases_input)
    return train_model(train_data)


def train_with_eval(input, **kwargs):
    lgb_train, lgb_eval = prepare_train_and_eval(input)
    return train_model(lgb_train, eval_data=lgb_eval, **kwargs)
