from typing import Set
import attr


@attr.s(auto_attribs=True, kw_only=True)
class Restrictions:
    c1_school_closing: int = attr.ib()
    c2_workplace_closing: int = attr.ib()
    c3_cancel_public_events: int = attr.ib()
    c4_restrictions_on_gatherings: int = attr.ib()
    c5_close_public_transport: int = attr.ib()
    c6_stay_at_home_requirements: int = attr.ib()
    c7_restrictions_on_internal_movement: int = attr.ib()
    c8_international_travel_controls: int = attr.ib()
    e1_income_support: int = attr.ib()
    e2_debt_contract_relief: int = attr.ib()
    h1_public_information_campaigns: int = attr.ib()
    h2_testing_policy: int = attr.ib()
    h3_contact_tracing: int = attr.ib()
    h6_facial_coverings: int = attr.ib()
    h7_vaccination_policy: int = attr.ib()
    h8_protection_of_elderly_people: int = attr.ib()

    def to_json(self):
        return self.__dict__

    @classmethod
    def from_json(cls, data):
        filtered = {kw: arg for kw, arg in data.items() if kw in cls.get_attrs()}
        return cls(**filtered)

    @classmethod
    def get_attrs(cls) -> Set:
        return {
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
            "h1_public_information_campaigns",
            "h2_testing_policy",
            "h3_contact_tracing",
            "h6_facial_coverings",
            "h7_vaccination_policy",
            "h8_protection_of_elderly_people",
        }
