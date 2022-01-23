N_PREDICTION_DAYS = 90
N_BUCKETS = 9
N_INPUT_DAYS = 7
MODEL_NUM_ROUNDS = 915
MODEL_PARAMS = {
    "boosting_type": "gbdt",
    "objective": "regression",
    "device_type": "cpu",
    "metric": {"l2", "l1", "mape"},
    "num_leaves": 8,
    "learning_rate": 0.002,
    "feature_fraction": 0.95,
    "bagging_fraction": 0.5,
    "bagging_freq": 15,
    "verbose": 1
}

COVID_FILE = "../data/covid_full.csv"
INPUT_FILE = "../data/confirmed_cases_input.csv"
TRAIN_DATA_FILE = "../data/train_data.bin"
MODEL_FILE = "../data/model.txt"

DATA_FILE_URL = "https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_latest.csv"

OXFORD_FILE_COLUMNS = [
    "C1_School closing",
    "C2_Workplace closing",
    "C3_Cancel public events",
    "C4_Restrictions on gatherings",
    "C5_Close public transport",
    "C6_Stay at home requirements",
    "C7_Restrictions on internal movement",
    "C8_International travel controls",
    "E1_Income support",
    "E2_Debt/contract relief",
    "E3_Fiscal measures",
    "E4_International support",
    "H1_Public information campaigns",
    "H2_Testing policy",
    "H3_Contact tracing",
    "H4_Emergency investment in healthcare",
    "H5_Investment in vaccines",
    "H6_Facial Coverings",
    "H7_Vaccination policy",
    "H8_Protection of elderly people",
    "C1_Flag",
    "C2_Flag",
    "C3_Flag",
    "C4_Flag",
    "C5_Flag",
    "C6_Flag",
    "C7_Flag",
    "E1_Flag",
    "H1_Flag",
    "H6_Flag",
    "H7_Flag",
    "H8_Flag",
    "CountryName",
    "CountryCode",
    "RegionName",
    "RegionCode",
    "Jurisdiction",
    "Date",
    "ConfirmedCases",
    "ConfirmedDeaths"
]

RESTRICTION_COLUMNS = [
    "c1_school_closing",
    "c2_workplace_closing",
    "c3_cancel_public_events",
    "c4_restrictions_on_gatherings",
    "c5_close_public_transport",
    "c6_stay_at_home_requirements",
    "c7_restrictions_on_internal_movement",
    "c8_international_travel_controls",
    "e1_income_support",
    "e2_debt_contract_relief",
    "e3_fiscal_measures",
    "e4_international_support",
    "h1_public_information_campaigns",
    "h2_testing_policy",
    "h3_contact_tracing",
    "h4_emergency_investment_in_healthcare",
    "h5_investment_in_vaccines",
    "h6_facial_coverings",
    "h7_vaccination_policy",
    "h8_protection_of_elderly_people",
]

FLAG_COLUMNS = [
    "c1_flag",
    "c2_flag",
    "c3_flag",
    "c4_flag",
    "c5_flag",
    "c6_flag",
    "c7_flag",
    "e1_flag",
    "h1_flag",
    "h6_flag",
    "h7_flag",
    "h8_flag",
]

INPUT_COLUMNS = RESTRICTION_COLUMNS + FLAG_COLUMNS
