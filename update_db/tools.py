import pandas as pd
from db import get_engine
from model import preprocess_confirmed_cases_input, prepare_train_data
from dotenv import load_dotenv
load_dotenv('../.env')

COVID_FILE = "../data/covid_full.csv"
INPUT_FILE = "../data/confirmed_cases_input.csv"


def get_covid_full():
    engine = get_engine()
    df = pd.read_sql('SELECT * FROM covid_full', con=engine)
    df.to_csv(COVID_FILE, index=False)    


def get_input():
    df = pd.read_csv(COVID_FILE)
    confirmed_cases_input = preprocess_confirmed_cases_input(df)
    confirmed_cases_input.to_csv(INPUT_FILE, index=False)


def get_train_data():
    df = pd.read_csv(INPUT_FILE)
    train_data = prepare_train_data(df)
    train_data.save_binary('../data/train_data.bin')


if __name__ == "__main__":
    get_input()
    # get_covid_full()
