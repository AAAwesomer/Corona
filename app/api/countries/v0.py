import logging
import datetime
from flask import Response, request, jsonify, make_response
from flask.blueprints import Blueprint
from app.models.restrictions import Restrictions
from app.db import db

LOGGER = logging.getLogger(__name__)

countries_bp = Blueprint('main', __name__, url_prefix='/api/countries')


@countries_bp.route('/', methods=['GET'])
def countries() -> Response:
    return make_response(jsonify(db.get_countries()))


@countries_bp.route('/<country_id>', methods=['GET'])
def country(country_id) -> Response:
    details = db.get_country_details(country_id)
    timeseries = db.get_country_timeseries(country_id)
    return make_response(jsonify({"details": details, "timeseries": timeseries}))


@countries_bp.route('/<country_id>/predict', methods=['GET'])  #TODO: CHANGE TO POST
def predict(country_id) -> Response:
    """
    Parse the request arguments and call the helper method to execute a prospect company search
    :return: a Response created with the results from the helper method
    """
    model_params = Restrictions.from_json({
        "c1_school_closing": 0,
        "c2_workplace_closing": 0,
        "c3_cancel_public_events": 0,
        "c4_restrictions_on_gatherings": 0,
        "c5_close_public_transport": 0,
        "c6_stay_at_home_requirements": 0,
        "c7_restrictions_on_internal_movement": 0,
        "c8_international_travel_controls": 0,
        "e1_income_support": 0,
        "e2_debt_contract_relief": 0,
        "h1_public_information_campaigns": 0,
        "h2_testing_policy": 0,
        "h3_contact_tracing": 0,
        "h6_facial_coverings": 0,
        "h7_vaccination_policy": 0,
        "h8_protection_of_elderly_people": 0,
    })
    # model_params = ModelParams.from_json(request.get_json())
    LOGGER.info(model_params)
    # model = get_model()
    # processed_input = process_input(model_params)
    # prediction = make_prediction(model, processed_input)
    return make_response(jsonify({'message': 'success',
                                  'predictions': test_predictions()}))


def get_model():
    return


def process_input(model_params):
    return


def make_prediction(model, processed_input):
    return


def test_predictions():
    predictions = []
    first_date = datetime.date.today() - datetime.timedelta(days=10)
    for i in range(100):
        date = first_date + datetime.timedelta(days=i)
        predictions.append({'date': date.strftime("%Y-%m-%d"), 'confirmed_cases': i})
    return predictions
