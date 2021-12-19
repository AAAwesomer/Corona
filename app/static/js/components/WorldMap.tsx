import React, { memo } from 'react';
import { Link } from 'react-router-dom';
import {
  ZoomableGroup,
  ComposableMap,
  Geographies,
  Geography,
} from 'react-simple-maps';

const geoUrl =
  'https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json';

const WorldMap = ({ setTooltipContent }) => {
  const rounded = (num: number) => {
    if (num > 1000000000) {
      return Math.round(num / 100000000) / 10 + 'Bn';
    } else if (num > 1000000) {
      return Math.round(num / 100000) / 10 + 'M';
    } else {
      return Math.round(num / 100) / 10 + 'K';
    }
  };

  return (
    <ComposableMap className="world-map" data-tip="" projectionConfig={{ scale: 200 }}>
      <ZoomableGroup zoom={1}>
        <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map((geo) => {
              const { NAME, POP_EST, ISO_A3 } = geo.properties;
              return (
                <Link key={geo.rsmKey} to={`/countries/${ISO_A3}`}>
                  <Geography
                    geography={geo}
                    onMouseEnter={() => {
                      setTooltipContent(`${NAME} — ${rounded(POP_EST)}`);
                    }}
                    onMouseLeave={() => {
                      setTooltipContent('');
                    }}
                    style={{
                      default: {
                        fill: '#D6D6DA',
                        stroke: 'white',
                        strokeWidth: '1px',
                        outline: 'none',
                      },
                      hover: {
                        stroke: 'white',
                        strokeWidth: '1px',
                        fill: '#F53',
                        outline: 'none',
                      },
                    }}
                  />
                </Link>
              );
            })
          }
        </Geographies>
      </ZoomableGroup>
    </ComposableMap>
  );
};

export default memo(WorldMap);
