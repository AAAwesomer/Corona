from argparse import ArgumentParser
from collections import OrderedDict
import pandas as pd
from dotenv import load_dotenv
load_dotenv("../.env")

from upkeep.db import get_engine
import upkeep.model as model
import upkeep.constants as constants


def get_covid_full():
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM covid_full", con=engine)
    df.to_csv(constants.COVID_FILE, index=False)


def get_input():
    df = pd.read_csv(constants.COVID_FILE)
    confirmed_cases_input = model.preprocess_confirmed_cases_input(df)
    confirmed_cases_input.to_csv(constants.INPUT_FILE, index=False)


def get_train_data():
    df = pd.read_csv(constants.INPUT_FILE)
    train_data = model.prepare_train_data(df)
    train_data.save_binary(constants.TRAIN_DATA_FILE)


def get_model():
    train_data = model.load_train_data(constants.TRAIN_DATA_FILE)
    bst = model.train_model(train_data)
    bst.save_model(constants.MODEL_FILE)


def get_all():
    get_covid_full()
    get_input()
    get_train_data()
    get_model()


def get_files(files):
    for file, func in FUNCTIONS.items():
        if file in files:
            func()


def parse_args():
    parser = ArgumentParser(description="Get files for development")
    parser.add_argument("files", nargs="+", choices=list(FUNCTIONS.keys()),
                        help="Files to get")
    return parser.parse_args()


if __name__ == "__main__":
    FUNCTIONS = OrderedDict(
        covid_full=get_covid_full,
        input=get_input,
        train_data=get_train_data,
        model=get_model,
        all=get_all
    )

    args = parse_args()
    if "all" in args.files:
        get_all()
    else:
        get_files(args.files)
