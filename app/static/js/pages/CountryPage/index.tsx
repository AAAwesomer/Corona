// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Restrictions } from 'lib/restrictions';
import { Country, getCountry } from 'lib/country';
import RestrictionController from 'components/RestrictionController';

const CountryPage: React.FC<any> = () => {
  let { id } = useParams();

  const [restrictions, setRestrictions] = useState<Restrictions | null>(null);
  const [country, loading] = getCountry(id);

  useEffect(() => {
    console.log(country?.details);
    if (country) setRestrictions(country.details.restrictions);
  }, [country]);

  const handleRestrictionChange = (restrictionId: string, value: number) => {
    setRestrictions({ ...restrictions!, [restrictionId]: value });
  };

  const renderDetails = (country: Country) => {
    const { name, date, confirmed_cases, confirmed_deaths } = country.details;
    return (
      <div className="country-details card">
        <div className="header">
          <h1>{name}</h1>
          <span className="date">Updated: {date}</span>
        </div>
        <div className="statistics">
          <div className="statistic">
            <h3>Confirmed Cases</h3>
            <div className="value">{confirmed_cases}</div>
          </div>
          <div className="statistic">
            <h3>Confirmed Deaths</h3>
            <div className="value">{confirmed_deaths}</div>
          </div>
        </div>
      </div>
    );
  };

  return (
    <main>
      {country && renderDetails(country)}
      {restrictions && (
        <RestrictionController
          restrictions={restrictions}
          handleChange={handleRestrictionChange}
        />
      )}
    </main>
  );
};

export default CountryPage;
