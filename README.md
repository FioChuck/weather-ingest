# Overview

TL;DR
A simple Python GCP Cloud Function used to pull weather data from https://openweathermap.org/api, unnest, and write results to PostgreSQL running in Google Cloud SQL.

This project was built to emulate transactions on an OLTP system for demos.

An example OpenWeatherMap API response is shown below. The cloud function selects a subset of the attributes and writes to a predefined SQL table _(see table definition below)_.

```json
{
  "coord": {
    "lon": 10.99,
    "lat": 44.34
  },
  "weather": [
    {
      "id": 501,
      "main": "Rain",
      "description": "moderate rain",
      "icon": "10d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 298.48,
    "feels_like": 298.74,
    "temp_min": 297.56,
    "temp_max": 300.05,
    "pressure": 1015,
    "humidity": 64,
    "sea_level": 1015,
    "grnd_level": 933
  },
  "visibility": 10000,
  "wind": {
    "speed": 0.62,
    "deg": 349,
    "gust": 1.18
  },
  "rain": {
    "1h": 3.16
  },
  "clouds": {
    "all": 100
  },
  "dt": 1661870592,
  "sys": {
    "type": 2,
    "id": 2075663,
    "country": "IT",
    "sunrise": 1661834187,
    "sunset": 1661882248
  },
  "timezone": 7200,
  "id": 3163858,
  "name": "Zocca",
  "cod": 200
}
```

# Setup

This project includes a yaml file for deployment to Google Cloud using Github Actions maintained here: https://github.com/google-github-actions/deploy-cloud-functions. The Github Action Workflow requires several _"Action Secrets"_ used to set environment variables during deployment. Set the following secrets in the repository before deployment.

| Action Secret  | Value                                                          |
| -------------- | -------------------------------------------------------------- |
| API_KEY        | Open Weather API Key Issued _(authenticate to data source)_    |
| DB_HOST        | PostgreSQL Public IP Address                                   |
| DB_PASS        | PostgreSQL User Password                                       |
| DB_USER        | PostgreSQL Username                                            |
| GCP_PROJECT_ID | GCP Project ID where Function will be deployed                 |
| GCP_SA_KEY     | Service Account Key used to authenticate GitHub to GCP Project |

API_KEY: This value is created by visiting https://openweathermap.org/api. First create and account and access your personalized key here: https://home.openweathermap.org/api_keys.

# PostgreSQL setup

Prior to deploying the cloud function, a destination table in PostgreSQL is required with the following schema. This table will act as the destination for data retrieved from the Open Weather API.

```SQL
CREATE TABLE open_weather_api (
    id integer GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    lon double precision,
    lat double precision,
    desc_short CHARACTER varying,
    desc_long CHARACTER varying,
    TEMP double precision,
    feels_like double precision,
    temp_min double precision,
    temp_max double precision,
    pressure double precision,
    humidity double precision,
    visibility double precision,
    wind_speed double precision,
    wind_deg double precision,
    clouds double precision,
    dt integer,
    sunrise integer,
    sunset integer,
    timezone integer,
    city CHARACTER varying,
    processing_time timestamp WITHOUT TIME ZONE
)
```

A PostgreSQL User is also required for cloud function authentication. The user and password are defined as GitHub Action Secrets. Ensure the user has the correct privileges _(see example below)_.

```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA schema_name TO username;
```
