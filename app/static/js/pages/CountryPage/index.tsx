// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import { getInitialInputs, InputValues } from 'lib/inputs';
import InputController from 'components/InputController';

const CountryPage: React.FC<any> = () => {
  let { id } = useParams();
  console.log(id);

  const [inputs, setInputs] = useState<InputValues>(getInitialInputs());

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
