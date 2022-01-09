DATA_FILE_URL = 'https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_latest.csv'
RESTRICTION_COLUMNS = [
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
]
FLAG_COLUMNS = [
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
]
INPUT_COLUMNS = RESTRICTION_COLUMNS + FLAG_COLUMNS
ALL_COLUMNS = INPUT_COLUMNS + ['CountryName', 'CountryCode', 'RegionName', 'RegionCode', 'Jurisdiction', 'Date', 'ConfirmedCases', 'ConfirmedDeaths']
