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

export interface TSItem {
  date: string;
}

export interface CountryTSItem {
  date: string;
  confirmed_cases: number;
  confirmed_deaths: number;
}

export interface Country {
  details: CountryDetails;
  timeseries: CountryTSItem[];
}

export interface CountryDetails {
  id: string;
  name: string;
  date: string;
  confirmed_cases: number;
  confirmed_deaths: number;
  restrictions: Restrictions;
}

export const getCountry = (id: string): [Country | null, boolean] => {
  const [country, setCountry] = useState<Country | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function fetchCountry() {
      try {
        setLoading(true);
        const country = await axios
          .get(`${BASE_URL}/${id}`)
          .then((response) => response.data);
        // console.log(json);
        setCountry(country);
      } catch (error) {
        setLoading(false);
      }
    }

    if (id) {
      fetchCountry();
    }
  }, [id]);

  return [country, loading];
};
