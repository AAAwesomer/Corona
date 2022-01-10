import logging
import datetime
from flask import Response, request, jsonify, make_response
from flask.blueprints import Blueprint
from marshmallow.exceptions import ValidationError
from app.models.predict_request import PredictRequestSchema
from app.db import db

LOGGER = logging.getLogger(__name__)

countries_bp = Blueprint('main', __name__, url_prefix='/api/countries')


@countries_bp.route('/', methods=['GET'])
def countries() -> Response:
    return make_response(jsonify(db.get_countries()))


@countries_bp.route('/<country_id>', methods=['GET'])
def country(country_id) -> Response:
    details, restrictions = db.get_country_info(country_id)
    timeseries = db.get_country_timeseries(country_id)
    return make_response(jsonify({"details": details,
                                  "restrictions": restrictions,
                                  "timeseries": timeseries}))


@countries_bp.route('/<country_id>/predict', methods=['POST'])
def predict(country_id) -> Response:
    """
    Parse the request arguments and call the helper method to execute a prospect company search
    :return: a Response created with the results from the helper method
    """
    request_json = request.get_json()
    print(list(PredictRequestSchema().fields.keys()))
    try:
        PredictRequestSchema().load(request_json)
    except ValidationError as e:
        return make_response(jsonify(e.messages), 400)
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
