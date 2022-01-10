from marshmallow import Schema, fields


class RestrictionsSchema(Schema):
    c1_school_closing = fields.Integer(required=True)
    c2_workplace_closing = fields.Integer(required=True)
    c3_cancel_public_events = fields.Integer(required=True)
    c4_restrictions_on_gatherings = fields.Integer(required=True)
    c5_close_public_transport = fields.Integer(required=True)
    c6_stay_at_home_requirements = fields.Integer(required=True)
    c7_restrictions_on_internal_movement = fields.Integer(required=True)
    c8_international_travel_controls = fields.Integer(required=True)
    e1_income_support = fields.Integer(required=True)
    e2_debt_contract_relief = fields.Integer(required=True)
    h1_public_information_campaigns = fields.Integer(required=True)
    h2_testing_policy = fields.Integer(required=True)
    h3_contact_tracing = fields.Integer(required=True)
    h6_facial_coverings = fields.Integer(required=True)
    h7_vaccination_policy = fields.Integer(required=True)
    h8_protection_of_elderly_people = fields.Integer(required=True)
