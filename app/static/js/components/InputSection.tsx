// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import React from 'react';
import { InputConfig, SectionConfig } from 'config/types';
import ModelInput from './ModelInput';

export interface InputSectionProps {
  config: SectionConfig;
  handleChange: (inputId: string, value: number) => void;
}

const InputSection: React.FC<InputSectionProps> = ({
  config,
  handleChange,
}) => {
  return (
    <div className="input-section">
      <h3>{config.name}</h3>
      <div className="model-inputs">
        {config.inputs.map((input: InputConfig, i: number) => (
          <ModelInput key={i} config={input} handleChange={handleChange} />
        ))}
      </div>
    </div>
  );
};

export default InputSection;
