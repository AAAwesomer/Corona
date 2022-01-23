from datetime import datetime, timedelta
import logging
from google.cloud import storage
from flask import current_app as app
import pandas as pd
import lightgbm as lgb
from app.db import db

LOGGER = logging.getLogger(__name__)


FILLER_COLUMNS = {
    "e3_fiscal_measures": 0,
    "e4_international_support": 0,
    "h4_emergency_investment_in_healthcare": 0,
    "h5_investment_in_vaccines": 0,
    "c1_flag": 1,
    "c2_flag": 1,
    "c3_flag": 1,
    "c4_flag": 1,
    "c5_flag": 1,
    "c6_flag": 1,
    "c7_flag": 1,
    "e1_flag": 1,
    "h1_flag": 1,
    "h6_flag": 1,
    "h7_flag": 1,
    "h8_flag": 1,
}


def load_model_from_storage():
    storage_client = storage.Client()
    bucket = storage_client.bucket(app.config["BUCKET"])
    blob = bucket.blob(app.config["MODEL_BLOB"])
    with open(app.config["MODEL_BLOB"], "wb") as f:
        blob.download_to_file(f)
    return app.config["MODEL_BLOB"]


def get_model():
    model_file = load_model_from_storage()
    return lgb.Booster(model_file=model_file)    


def get_input_and_current_cases(region_id, date, restrictions):
    recent_cases = db.get_country_recent_cases(region_id, date)
    date_to_value = {item["date"]: item["confirmed_cases"] for item in recent_cases}
    current_cases = date_to_value[date]
    dates_reversed = sorted(date_to_value.keys(), reverse=True)[1:]
    cases_columns = {"confirmed_cases_%s_days_ago" % (i + 1): date_to_value[d] / current_cases
                     for i, d in enumerate(dates_reversed)}
    input_row = dict(**restrictions, **cases_columns, **FILLER_COLUMNS)
    input = pd.DataFrame.from_records([input_row], index=list(range(90)))
    input = input.reset_index().rename(columns={"index": "prediction_window"})
    input["prediction_window"] += 1
    return input, current_cases


def predict(region_id, date, restrictions):
    input, current_cases = get_input_and_current_cases(region_id, date, restrictions)
    bst = get_model()
    predictions = bst.predict(input)
    d = datetime.strptime(date, "%Y-%m-%d")
    return [{
        "date": (d + timedelta(days=i + 1)).strftime("%Y-%m-%d"),
        "confirmed_cases": int(prediction * current_cases)
    } for i, prediction in enumerate(predictions)]
