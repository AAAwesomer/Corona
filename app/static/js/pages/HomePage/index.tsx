// Copyright Contributors to the Amundsen project.
// SPDX-License-Identifier: Apache-2.0

import React, { useEffect, useState } from 'react';
import WorldMap from 'components/WorldMap';
import ReactTooltip from 'react-tooltip';

export const useMousePosition = () => {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const setFromEvent = (e) => setPosition({ x: e.clientX, y: e.clientY });
    window.addEventListener('mousemove', setFromEvent);

    return () => {
      window.removeEventListener('mousemove', setFromEvent);
    };
  }, []);

  return position;
};

const HomePage: React.FC<any> = () => {
  const [content, setContent] = useState('');
  const mousePosition = useMousePosition();

  const getTooltipPosition = (
    position: { left: number; top: number },
    currentEvent: Event,
    currentTarget: EventTarget,
    // node is the ref argument, and the wrapper
    // is restricted to: div | span
    refNode: null | HTMLDivElement | HTMLSpanElement
  ) => {
    const offsetX = (refNode?.clientWidth || 0) / 2;
    return {
      left: mousePosition.x - offsetX,
      top: mousePosition.y - 40,
    };
  };

  return (
    <main>
      <ReactTooltip
        className="tooltip"
        place="top"
        overridePosition={getTooltipPosition}
      >
        {content}
      </ReactTooltip>
      <div className="info-box card">
        <h3>COVID-19 Map</h3>
        <p>Hover over the countries to view basic COVID-19 statistics.</p>
      </div>
      <WorldMap setTooltipContent={setContent} />
    </main>
  );
};

export default HomePage;
