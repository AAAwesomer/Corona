// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import React from 'react';
import appConfig from 'config/config';
import InputSection from './InputSection';

export interface InputValues {
  [input: string]: number;
}

export interface InputControllerProps {
  handleChange: (inputId: string, value: number) => void;
}

const InputController: React.FC<InputControllerProps> = ({ handleChange }) => {
  return (
    <div className="input-controller card">
      <div className="controller-container">
        <InputSection
          config={appConfig.inputSections[0]}
          handleChange={handleChange}
        />
      </div>
      <div className="controller-container">
        <InputSection
          config={appConfig.inputSections[1]}
          handleChange={handleChange}
        />
        <InputSection
          config={appConfig.inputSections[2]}
          handleChange={handleChange}
        />
      </div>
    </div>
  );
};

export default InputController;
