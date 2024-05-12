from data_fetch import DataFetcher
import numpy as np
import pandas as pd

class DataAnalysis:
    
    def __init__(self, lat, lon, year):
        self.lat = lat
        self.lon = lon
        self.year = year

    def daily_data(self):

        # Fetch the data
        data_fetcher = DataFetcher()
        data = data_fetcher.fetch_data(self.lat, self.lon, self.year)
        print(data)

        # Convert columns to numeric types
        data = data.apply(pd.to_numeric, errors='coerce')

        # Average data by Day
        # Convert 'Month' and 'Day' to integer
        data['Month'] = data['Month'].astype(int)
        data['Day'] = data['Day'].astype(int)
        data['Hour'] = data['Hour'].astype(int)

        # Group by 'Day' and calculate mean
        daily_data = data.groupby(['Month', 'Day', 'Hour']).mean().reset_index()
        print(daily_data)
        return daily_data

    def monthly_data(self):
        # Fetch the data
        data_fetcher = DataFetcher()
        data = data_fetcher.fetch_data(self.lat, self.lon, self.year)
        print(data)

        # Convert columns to numeric types
        data = data.apply(pd.to_numeric, errors='coerce')

        # Average data by Month
        # Convert 'Month' and 'Day' to integer
        data['Month'] = data['Month'].astype(int)
        data['Day'] = data['Day'].astype(int)

        # Group by both 'Month' and 'Day' and calculate mean
        monthly_data = data.groupby(['Month', 'Day']).mean().reset_index()

        return monthly_data
    
# Test
# DataAnalysis().monthly_data(31.9686, -99.9018, 2012)
DataAnalysis(31.9686, -99.9018, 2012).monthly_data()

