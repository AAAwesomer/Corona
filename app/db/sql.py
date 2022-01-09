"""SQL queries
"""

get_countries = """
    SELECT
      cf.region_id AS id,
      DATE_FORMAT(cf.date, "%%Y-%%m-%%d") AS date,
      cf.confirmed_cases AS confirmed_cases,
      cf.confirmed_deaths AS confirmed_deaths
    FROM covid_full cf
    LEFT JOIN region ON region.id = cf.region_id
    INNER JOIN (
      SELECT region_id, MAX(date) AS date
      FROM covid_full
      WHERE confirmed_cases IS NOT NULL
        AND date < DATE_SUB(CURDATE(), INTERVAL 2 DAY)
      GROUP BY region_id
    ) cf2 ON cf.region_id = cf2.region_id AND cf.date = cf2.date
    WHERE region.type = 'NAT';
"""

get_country_details = """
    SELECT
      cf.region_id AS id,
      region.name AS name,
      cf.c1_school_closing AS c1_school_closing,
      cf.c2_workplace_closing AS c2_workplace_closing,
      cf.c3_cancel_public_events AS c3_cancel_public_events,
      cf.c4_restrictions_on_gatherings AS c4_restrictions_on_gatherings,
      cf.c5_close_public_transport AS c5_close_public_transport,
      cf.c6_stay_at_home_requirements AS c6_stay_at_home_requirements,
      cf.c7_restrictions_on_internal_movement AS c7_restrictions_on_internal_movement,
      cf.c8_international_travel_controls AS c8_international_travel_controls,
      cf.e1_income_support AS e1_income_support,
      cf.e2_debt_contract_relief AS e2_debt_contract_relief,
      cf.h1_public_information_campaigns AS h1_public_information_campaigns,
      cf.h2_testing_policy AS h2_testing_policy,
      cf.h3_contact_tracing AS h3_contact_tracing,
      cf.h6_facial_coverings AS h6_facial_coverings,
      cf.h7_vaccination_policy AS h7_vaccination_policy,
      cf.h8_protection_of_elderly_people AS h8_protection_of_elderly_people,
      cf.confirmed_cases AS confirmed_cases,
      cf.confirmed_deaths AS confirmed_deaths,
      DATE_FORMAT(cf.date, "%%Y-%%m-%%d") AS date
    FROM covid_full cf
    LEFT JOIN region ON region.id = cf.region_id
    INNER JOIN (
      SELECT region_id, MAX(date) AS date
      FROM covid_full
      WHERE region_id = %s
        AND confirmed_cases IS NOT NULL
        AND date < DATE_SUB(CURDATE(), INTERVAL 2 DAY)
    ) cf2 ON cf.region_id = cf2.region_id AND cf.date = cf2.date
"""

get_country_timeseries = """
    SELECT 
      DATE_FORMAT(date, "%%Y-%%m-%%d") AS date,
      coalesce(confirmed_cases, 0) AS confirmed_cases,
      coalesce(confirmed_deaths, 0) AS confirmed_deaths
    FROM covid_full
    WHERE region_id = %s
      AND confirmed_cases IS NOT NULL
      AND date < DATE_SUB(CURDATE(), INTERVAL 2 DAY);
"""
