// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import React, { useState } from 'react';
import { AppConfig } from 'config/types';
import InputController, { InputValues } from 'components/InputController';
import appConfig from 'config/config';
import { useParams } from 'react-router-dom';

const CountryPage: React.FC<any> = () => {
  let { id } = useParams();
  console.log(id)

  const getInitialInputs = (config: AppConfig) => {
    let inputs: InputValues = {};
    for (const section of config.inputSections) {
      for (const input of section.inputs) {
        inputs[input.id] = Math.min(
          ...Object.keys(input.coding).map((i) => parseInt(i))
        );
      }
    }
    return inputs;
  };

  const [inputs, setInputs] = useState<InputValues>(
    getInitialInputs(appConfig)
  );

  const handleInputChange = (inputId: string, value: number) => {
    setInputs({ ...inputs, [inputId]: value });
  };

  return (
    <main>
      <InputController handleChange={handleInputChange} />
    </main>
  );
};

export default CountryPage;
