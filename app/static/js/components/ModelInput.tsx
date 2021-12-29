// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import React, { useState } from 'react';
import { InputConfig } from 'config/types';
import { getCodingsKeys } from 'lib/inputs';

export interface InputProps {
  config: InputConfig;
  handleChange: (inputId: string, value: number) => void;
}

const ModelInput: React.FC<InputProps> = ({ config, handleChange }) => {
  const codingsKeys = getCodingsKeys(config);
  const min = Math.min(...codingsKeys);
  const max = Math.max(...codingsKeys);

  const [value, setValue] = useState(min);

  const onChange = (e) => {
    const newValue = parseInt(e.target.value);
    setValue(newValue);
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

export default ModelInput;
