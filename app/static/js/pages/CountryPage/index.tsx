// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Restrictions } from 'lib/restrictions';
import { useCountry, CountryState } from 'lib/country';
import RestrictionController from 'components/RestrictionController';
import CoronaGraph from 'components/CoronaGraph';

const CountryPage: React.FC<any> = () => {
  let { id } = useParams();

  const {
    details,
    restrictions,
    timeseries,
    predictions,
    loading,
    setRestrictions,
    predict,
  }: CountryState = useCountry(id);

  const handleRestrictionChange = (restrictionId: string, value: number) => {
    setRestrictions({ ...restrictions!, [restrictionId]: value });
  };

  const renderDetails = () => {
    const { name, date, confirmed_cases, confirmed_deaths } = details!;
    return (
      <div className="country-details padding-4 column-item card">
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
      {details && timeseries && (
        <>
          {renderDetails()}
          <CoronaGraph data={timeseries!} predictions={predictions || undefined} />
          <button className="btn-predict column-item" onClick={predict}>
            Predict
          </button>
        </>
      )}
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
