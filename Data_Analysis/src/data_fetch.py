import urllib.parse
import pandas as pd
from dotenv import load_dotenv
import os


class DataFetcher:
    def __init__(self):
        pass

    def fetch_data(self, lat, lon, year):
        # Load the environment variables
        load_dotenv()

        # API Key
        api_key = os.getenv('AUTH_TOKEN')
        email = os.getenv('EMAIL')

        # Define parameters: TEXAS: State with the highest wind energy generation
        # Source: https://www.eia.gov/energyexplained/wind/where-wind-power-is-harnessed.php
        # lat, lon, year = 31.9686, -99.9018, 2012
        attributes = 'windspeed_10m,windspeed_60m,windspeed_100m,windspeed_140m,windspeed_200m'
        interval = 60
        leap_day = 'true'
        utc = 'false'

        # Construct the WKT point
        wkt = f"POINT({lon} {lat})"

        # Base URL and query
        base_url = 'https://developer.nrel.gov/api/wind-toolkit/v2/wind/wtk-download.csv'
        query = {
            "api_key": api_key,
            "wkt": wkt,
            "names": year,
            "attributes": attributes,
            "interval": interval,
            "leap_day": leap_day,
            "email": email,
            "utc": utc
        }

        # Encode the query into URL
        query_string = urllib.parse.urlencode(query, safe=':/,')
        full_url = f"{base_url}?{query_string}"

        # Print the URL
        # print("URL for API request:", full_url)

        # Fetch the data
        try:
            data = pd.read_csv(full_url)
            # Use first row as header
            data.columns = data.iloc[0]
            data = data[1:]
            return data
        except Exception as e:
            print(f"An error occurred: {e}")


