import appConfig from 'config/config';
import { RestrictionConfig } from 'config/types';

export interface Restrictions {
  c1_school_closing: number;
  c2_workplace_closing: number;
  c3_cancel_public_events: number;
  c4_restrictions_on_gatherings: number;
  c5_close_public_transport: number;
  c6_stay_at_home_requirements: number;
  c7_restrictions_on_internal_movement: number;
  c8_international_travel_controls: number;
  e1_income_support: number;
  e2_debt_contract_relief: number;
  h1_public_information_campaigns: number;
  h2_testing_policy: number;
  h3_contact_tracing: number;
  h6_facial_coverings: number;
  h7_vaccination_policy: number;
  h8_protection_of_elderly_people: number;
}

export const getCodingsKeys = (restrictionConfig: RestrictionConfig) =>
  Object.keys(restrictionConfig.coding).map((i) => parseInt(i));

export const getInitialRestrictions = () => {
  let restrictions = {};
  for (const section of appConfig.restrictionSections) {
    for (const restriction of section.restrictions) {
      restrictions[restriction.id] = Math.min(...getCodingsKeys(restriction));
    }
  }
  return restrictions as Restrictions;
};
