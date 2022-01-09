export interface AppConfig {
  restrictionSections: SectionConfig[]
}

export interface Coding {
  [key: number]: string;
}

export interface RestrictionConfig {
  id: string;
  name: string;
  description: string;
  measurement: string;
  coding: Coding;
}

export interface SectionConfig {
  name: string;
  restrictions: RestrictionConfig[];
}
