import appConfig from 'config/config';
import { InputConfig } from 'config/types';

export interface InputValues {
  [input: string]: number;
}

export const getCodingsKeys = (inputConfig: InputConfig) =>
  Object.keys(inputConfig.coding).map((i) => parseInt(i));

export const getInitialInputs = () => {
  let inputs: InputValues = {};
  for (const section of appConfig.inputSections) {
    for (const input of section.inputs) {
      inputs[input.id] = Math.min(...getCodingsKeys(input));
    }
  }
  return inputs;
};
