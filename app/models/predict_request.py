from marshmallow import Schema, fields
from app.models.restrictions import RestrictionsSchema


class PredictRequestSchema(Schema):
    date = fields.DateTime(format="%Y-%m-%d", required=True)
    restrictions = fields.Nested(RestrictionsSchema(), required=True)
