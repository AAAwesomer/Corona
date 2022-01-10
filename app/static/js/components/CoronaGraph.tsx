import { ApexOptions } from 'apexcharts';
import { CountryTSItem, PredictionTSItem } from 'lib/country';
import React from 'react';
import Chart from 'react-apexcharts';

interface DataPoint {
  x: string;
  y: number;
}

interface CoronaGraphProps {
  data: CountryTSItem[];
  predictions?: PredictionTSItem[];
}

interface ChartConfig {
  series: any[];
  options: ApexOptions;
}

const CoronaGraph: React.FC<CoronaGraphProps> = ({ data, predictions }) => {
  const getPredictionSeries = () => {
    if (!predictions) return null;
    let predictionsData: DataPoint[] = [];
    for (const prediction of predictions) {
      predictionsData.push({
        x: prediction.date,
        y: prediction.confirmed_cases,
      });
    }
    return {
      name: 'Prediction',
      data: predictionsData,
    };
  };

  const getSeries = () => {
    const seriesObj = {};
    // initialize seriesObj with series configs for each plotted variable
    for (const variable of Object.keys(data[0])) {
      if (variable != 'date') {
        seriesObj[variable] = {
          name: variable,
          data: [],
        };
      }
    }
    // push variable values into respective series configs
    for (const tsItem of data) {
      for (const [variable, value] of Object.entries(tsItem)) {
        if (variable !== 'date') {
          seriesObj[variable]['data'].push({
            x: tsItem.date,
            y: value as number,
          });
        }
      }
    }
    const series = Object.values(seriesObj);
    // add predictions if provided
    const predictionSeries = getPredictionSeries();
    if (predictionSeries) series.push(predictionSeries);
    return series;
  };

  const config: ChartConfig = {
    series: getSeries(),
    options: {
      chart: {
        type: 'area',
        stacked: false,
        height: 350,
        zoom: {
          type: 'x',
          enabled: true,
          autoScaleYaxis: true,
        },
        toolbar: {
          autoSelected: 'zoom',
        },
      },
      dataLabels: {
        enabled: false,
      },
      markers: {
        size: 0,
      },
      title: {
        text: 'Coronavirus Progression',
        align: 'left',
      },
      fill: {
        type: 'gradient',
        gradient: {
          shadeIntensity: 1,
          inverseColors: false,
          opacityFrom: 0.5,
          opacityTo: 0,
          stops: [0, 90, 100],
        },
      },
      yaxis: {
        labels: {
          formatter: function (val) {
            return val.toFixed(0);
          },
        },
        title: {
          text: 'Total Cases/Deaths',
        },
      },
      xaxis: {
        type: 'datetime',
      },
      tooltip: {
        shared: false,
        y: {
          formatter: function (val) {
            return val.toFixed(0);
          },
        },
      },
    },
  };

  return (
    <div className="padding-4 column-item card">
      <Chart
        options={config.options}
        series={config.series}
        type="area"
        height={350}
      />
    </div>
  );
};

export default CoronaGraph;

// import React from 'react';
// import ReactFC from 'react-fusioncharts';
// import FusionCharts from 'fusioncharts';
// import TimeSeries from 'fusioncharts/fusioncharts.timeseries';
// import FusionTheme from 'fusioncharts/themes/fusioncharts.theme.fusion';
// import { CountryTSItem } from 'lib/country';

// ReactFC.fcRoot(FusionCharts, TimeSeries, FusionTheme);

// interface CoronaGraphProps {
//   data: CountryTSItem[];
// }

// const schema = [
//   {
//     name: 'date',
//     type: 'date',
//     format: '%Y-%m-%d',
//   },
//   {
//     name: 'confirmed_cases',
//     type: 'number',
//   },
//   {
//     name: 'confirmed_deaths',
//     type: 'number',
//   },
// ];

// const CoronaGraph: React.FC<CoronaGraphProps> = ({ data }) => {
//   const fusionTable = new FusionCharts.DataStore().createDataTable(
//     data,
//     schema
//   );
//   const chartConfig = {
//     type: 'timeseries',
//     renderAt: 'container',
//     width: '700',
//     height: '400',
//     dataFormat: 'json',
//     dataSource: {
//       caption: { text: 'Progression of CoVid-19' },
//       data: fusionTable,
//       yAxis: [
//         {
//           plot: [
//             {
//               value: 'Cases',
//             },
//           ],
//         },
//         {
//           plot: [
//             {
//               value: 'Deaths',
//             },
//           ],
//         },
//       ],
//     },
//   };
//   return <ReactFC {...chartConfig} />;
// };

// export default CoronaGraph;
