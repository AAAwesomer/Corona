export interface AppConfig {
  inputSections: SectionConfig[]
}

export interface Coding {
  [key: number]: string;
}

export interface InputConfig {
  id: string;
  name: string;
  description: string;
  measurement: string;
  coding: Coding;
}

export interface SectionConfig {
  name: string;
  inputs: InputConfig[];
}
