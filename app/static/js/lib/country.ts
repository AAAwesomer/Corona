import axios from 'axios';
import { useState, useEffect } from 'react';
import { Restrictions } from './restrictions';

const BASE_URL = '/api/countries';

export interface CountryDetails {
  id: string;
  name: string;
  date: string;
  confirmed_cases: number;
  confirmed_deaths: number;
  restrictions: Restrictions;
}

export interface PredictionTSItem {
  date: string;
  confirmed_cases: number;
}

export interface CountryTSItem {
  date: string;
  confirmed_cases: number;
  confirmed_deaths: number;
}

export interface CountryInfo {
  details: CountryDetails;
  restrictions: Restrictions;
  timeseries: CountryTSItem[];
}

export interface PredictionResult {
  message: string;
  predictions: PredictionTSItem[];
}

export interface CountryDetails {
  id: string;
  name: string;
  date: string;
  confirmed_cases: number;
  confirmed_deaths: number;
  restrictions: Restrictions;
}

export interface CountryState {
  details?: CountryDetails;
  restrictions?: Restrictions;
  predictions?: PredictionTSItem[];
  timeseries?: CountryTSItem[];
  loading: boolean;
  setRestrictions: (restrictions: Restrictions) => void;
  predict: () => void;
}

export const useCountry = (id: string): CountryState => {
  const [details, setDetails] = useState<CountryDetails | undefined>();
  const [restrictions, setRestrictions] = useState<Restrictions | undefined>();
  const [predictions, setPredictions] = useState<
    PredictionTSItem[] | undefined
  >();
  const [timeseries, setTimeseries] = useState<CountryTSItem[] | undefined>();
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function fetchCountry() {
      try {
        setLoading(true);
        const country: CountryInfo = await axios
          .get(`${BASE_URL}/${id}`)
          .then((response) => response.data);
        // console.log(json);
        setDetails(country.details);
        setRestrictions(country.restrictions);
        setTimeseries(country.timeseries);
      } catch (error) {}
      setLoading(false);
    }

    if (id) {
      fetchCountry();
    }
  }, [id]);

  // const setRestrictions = (restrictions: Restrictions) => setRestrictionsState(restrictions);

  const predict = async () => {
    try {
      const predictionResult: PredictionResult = await axios
        .get(`${BASE_URL}/${id}/predict`)
        .then((response) => response.data);
      // console.log(json);
      setPredictions(predictionResult.predictions);
    } catch (error) {}
  };

  return {
    details,
    restrictions,
    timeseries,
    predictions,
    loading,
    setRestrictions,
    predict,
  };
};
