import { AppConfig } from './types';

const appConfig: AppConfig = {
  inputSections: [
    {
      name: 'Containment and closure policies',
      inputs: [
        {
          id: 'C1_School closing',
          name: 'School closing',
          description: 'Closings of schools and universities',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No measures',
            1: 'Recommend closing or all schools open with alterations resulting in significant differences compared to non-covid-19 operations',
            2: 'Require closing (only some levels or categories, eg just high school, or just public schools)',
            3: 'Require closing all levels',
          },
        },
        {
          id: 'C2_Workplace closing',
          name: 'Workplace closing',
          description: 'Closings of workplaces',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No measures',
            1: 'Recommend closing (or recommend work from home) or all businesses open with alterations resulting in significant differences compared to non-covid-19 operation',
            2: 'Require closing (or work from home) for some sectors or categories of workers',
            3: 'Require closing (or work from home) for all-but-essential workplaces (eg grocery stores, doctors)',
          },
        },
        {
          id: 'C3_Cancel public events',
          name: 'Cancel public events',
          description: 'Cancelling public events',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No measures',
            1: 'Recommend cancelling',
            2: 'Require cancelling',
          },
        },
        {
          id: 'C4_Restrictions on gatherings',
          name: 'Restrictions on gatherings',
          description: 'Limits on gatherings',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No restrictions',
            1: 'Restrictions on very large gatherings (the limit is above 1000 people)',
            2: 'Restrictions on gatherings between 101-1000 people',
            3: 'Restrictions on gatherings between 11-100 people',
            4: 'Restrictions on gatherings of 10 people or less',
          },
        },
        {
          id: 'C5_Close public transport',
          name: 'Close public transport',
          description: 'Closing of public transport',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No measures',
            1: 'Recommend closing (or significantly reduce volume/route/means of transport available)',
            2: 'Require closing (or prohibit most citizens from using it)',
          },
        },
        {
          id: 'C6_Stay at home requirements',
          name: 'Stay at home requirements',
          description:
            'Orders to "shelter-in-place" and otherwise confine to the home',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No measures',
            1: 'Recommend not leaving house',
            2: "Require not leaving house with exceptions for daily exercise, grocery shopping, and 'essential' trips",
            3: 'Require not leaving house with minimal exceptions (eg allowed to leave once a week, or only one person can leave at a time, etc)',
          },
        },
        {
          id: 'C7_Restrictions on internal movement',
          name: 'Restrictions on internal movement',
          description:
            'Restrictions on internal movement between cities/regions',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No measures',
            1: 'Recommend not to travel between regions/cities',
            2: 'Internal movement restrictions in place',
          },
        },
        {
          id: 'C8_International travel controls',
          name: 'International travel controls',
          description:
            'Restrictions on international travel. Note: accounts for foreign travellers, not citizens',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No restrictions',
            1: 'Screening arrivals',
            2: 'Quarantine arrivals from some or all regions',
            3: 'Ban arrivals from some regions',
            4: 'Ban on all regions or total border closure',
          },
        },
      ],
    },
    {
      name: 'Economic policies',
      inputs: [
        {
          id: 'E1_Income support <br/>(for households)',
          name: 'Income support (for households)',
          description:
            'Whether the government is providing direct cash payments to people who lose their jobs or cannot work.',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No income support',
            1: 'Government is replacing less than 50% of lost salary (or if a flat sum, it is less than 50% median salary)',
            2: 'Government is replacing 50% or more of lost salary (or if a flat sum, it is greater than 50% median salary)',
          },
        },
        {
          id: 'E2_Debt/contract relief <br/>(for households)',
          name: 'Debt/contract relief (for households)',
          description:
            'Whether the government is freezing financial obligations for households (eg stopping loan repayments, preventing services like water from stopping, or banning evictions)',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No debt/contract relief',
            1: 'Narrow relief, specific to one kind of contract',
            2: 'Broad debt/contract relief',
          },
        },
      ],
    },
    {
      name: 'Health system policies',
      inputs: [
        {
          id: 'H1_Public information campaigns',
          name: 'Public information campaigns',
          description: 'Presence of public info campaigns',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No covid-19 public information campaign',
            1: 'Public officials urging caution about covid-19',
            2: 'Coordinated public information campaign (eg across traditional and social media)',
          },
        },
        {
          id: 'H2_Testing policy',
          name: 'Testing policy',
          description:
            'Government policy on who has access to testing. Note: Does not cover testing for immunity (antibody test)',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No testing policy',
            1: 'Only those who both (a) have symptoms and (b) meet specific criteria (eg key workers, admitted to hospital, came into contact with a known case, returned from overseas)',
            2: 'Testing of anyone showing covid-19 symptoms',
            3: 'Open public testing (eg "drive through" testing available to asymptomatic people)',
          },
        },
        {
          id: 'H3_Contact tracing',
          name: 'Contact tracing',
          description:
            'Government policy on contact tracing after a positive diagnosis. Note: we are looking for policies that would identify all people potentially exposed to Covid-19; voluntary bluetooth apps are unlikely to achieve this',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No contact tracing',
            1: 'Limited contact tracing; not done for all cases',
            2: 'Comprehensive contact tracing; done for all identified cases',
          },
        },
        {
          id: 'H6_Facial Coverings',
          name: 'Facial Coverings',
          description:
            'Policies on the use of facial coverings outside the home',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No policy',
            1: 'Recommended',
            2: 'Required in some specified shared/public spaces outside the home with other people present, or some situations when social distancing not possible',
            3: 'Required in all shared/public spaces outside the home with other people present or all situations when social distancing not possible',
            4: 'Required outside the home at all times regardless of location or presence of other people',
          },
        },
        {
          id: 'H7_Vaccination Policy',
          name: 'Vaccination Policy',
          description:
            'Policies for vaccine delivery for different groups',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No availability',
            1: 'Availability for one of following: key workers/ clinically vulnerable groups (non elderly) / elderly groups',
            2: 'Availability for two of following: key workers/ clinically vulnerable groups (non elderly) / elderly groups',
            3: 'Availability for all of following: key workers/ clinically vulnerable groups (non elderly) / elderly groups',
            4: 'Availability for all three plus partial additional availability (select broad groups/ages)',
            5: 'Universal availability',
          },
        },
        {
          id: 'H8_Protection of elderly people',
          name: 'Protection of elderly people',
          description:
            'Policies for protecting elderly people (as defined locally) in Long Term Care Facilities and/or the community and home setting',
          measurement: 'Ordinal scale',
          coding: {
            0: 'No measures',
            1: 'Recommended isolation, hygiene, and visitor restriction measures in ltcfs and/or elderly  people to stay at home',
            2: 'Narrow restrictions for isolation, hygiene in ltcfs, some limitations on external visitors and/or restrictions protecting elderly people at home',
            3: 'Extensive restrictions for isolation and hygiene in ltcfs, all non-essential external visitors prohibited, and/or all elderly people required to stay at home and not leave the home with minimal exceptions, and receive no external visitors',
          },
        },
      ],
    },
  ],
};

export default appConfig;
