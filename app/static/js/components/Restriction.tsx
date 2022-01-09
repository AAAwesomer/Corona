// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import React from 'react';
import { RestrictionConfig } from 'config/types';
import { getCodingsKeys } from 'lib/restrictions';

export interface RestrictionProps {
  config: RestrictionConfig;
  value: number;
  handleChange: (restrictionId: string, value: number) => void;
}

const Restriction: React.FC<RestrictionProps> = ({
  config,
  value,
  handleChange,
}) => {
  const codingsKeys = getCodingsKeys(config);
  const min = Math.min(...codingsKeys);
  const max = Math.max(...codingsKeys);

  const onChange = (e) => {
    const newValue = parseInt(e.target.value);
    handleChange(config.id, newValue);
  };

  return (
    <div className="model-input">
      <h4>{config.name}</h4>
      <div className="description">{config.description}</div>
      <input
        type="range"
        min={min}
        max={max}
        value={value}
        onChange={onChange}
        className="slider"
      />
      <div className="value-info">
        <div className="value">{value} -</div>
        <div>{config.coding[value]}</div>
      </div>
    </div>
  );
};

export default Restriction;
