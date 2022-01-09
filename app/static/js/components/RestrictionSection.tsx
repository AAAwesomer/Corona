// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import React from 'react';
import { RestrictionConfig, SectionConfig } from 'config/types';
import Restriction from './Restriction';
import { Restrictions } from 'lib/restrictions';

export interface RestrictionSectionProps {
  restrictions: Restrictions;
  config: SectionConfig;
  handleChange: (restrictionId: string, value: number) => void;
}

const RestrictionSection: React.FC<RestrictionSectionProps> = ({
  restrictions,
  config,
  handleChange,
}) => {
  return (
    <div className="input-section">
      <h3>{config.name}</h3>
      <div className="model-inputs">
        {config.restrictions.map(
          (restriction: RestrictionConfig, i: number) => (
            <Restriction
              key={i}
              config={restriction}
              value={restrictions[restriction.id]}
              handleChange={handleChange}
            />
          )
        )}
      </div>
    </div>
  );
};

export default RestrictionSection;
