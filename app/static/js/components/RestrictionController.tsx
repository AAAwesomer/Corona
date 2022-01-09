// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import React from 'react';
import appConfig from 'config/config';
import RestrictionSection from './RestrictionSection';
import { Restrictions } from 'lib/restrictions';

export interface RestrictionControllerProps {
  restrictions: Restrictions;
  handleChange: (restrictionId: string, value: number) => void;
}

const RestrictionController: React.FC<RestrictionControllerProps> = ({
  restrictions,
  handleChange,
}) => {
  return (
    <div className="input-controller card">
      <div className="controller-container">
        <RestrictionSection
          restrictions={restrictions}
          config={appConfig.restrictionSections[0]}
          handleChange={handleChange}
        />
      </div>
      <div className="controller-container">
        <RestrictionSection
          restrictions={restrictions}
          config={appConfig.restrictionSections[1]}
          handleChange={handleChange}
        />
        <RestrictionSection
          restrictions={restrictions}
          config={appConfig.restrictionSections[2]}
          handleChange={handleChange}
        />
      </div>
    </div>
  );
};

export default RestrictionController;
