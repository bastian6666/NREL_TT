# NREL_TT

## Welcome to my technical task repository

The repository is organized into two main sections:

### Data Analysis

This section contains two Python scripts and a Jupyter notebook.

The `data_fetch.py` file contains a Python class `DataFetcher` that is responsible for fetching wind data from the NREL Wind Toolkit Data V2 (Source: https://developer.nrel.gov/docs/wind/wind-toolkit/wtk-download/).

1. **Initialization**: The `DataFetcher` class has an `__init__` method that initializes the class. 

2. **Fetching data**: The `fetch_data` method is responsible for fetching the wind data. It takes in latitude, longitude, and year as parameters.

    - Loads environment variables using the `load_dotenv` function. This is where it gets the API key and email from.

    - Sets up the parameters for the API request. These include the attributes (different wind speeds at different heights), the interval, whether to include leap day data, and whether the time should be in UTC.

    - Constructs a Well-Known Text (WKT) point using the provided latitude and longitude. This point is used in the API request.

    - Constructs the base URL and query for the API request. The query includes the API key, WKT point, year, attributes, interval, leap day, email, and UTC parameters.

    - Encodes the query into a URL and appends it to the base URL to form the full URL for the API request.

    - Fetches the data from the API using the `pd.read_csv` function, which reads the data into a pandas DataFrame. The first row of the data is used as the header.

The `data_analysis.py` file contains a Python class `DataAnalysis` that is responsible for analyzing wind data.

1. **Initialization**: The `DataAnalysis` class has an `__init__` method that initializes the class with latitude, longitude, and year.

2. **Daily Data Analysis**: The `daily_data` method fetches the wind data for the given latitude, longitude, and year using the `DataFetcher` class. It then converts the data columns to numeric types, groups the data by month, day, and hour, and calculates the mean for each group. The resulting daily data is then returned.

3. **Monthly Data Analysis**: The `monthly_data` method fetches the wind data for the given latitude, longitude, and year using the `DataFetcher` class. It then converts the data columns to numeric types, groups the data by month and day, and calculates the mean for each group. The resulting monthly data is then returned.

The `wind_analysis.ipynb` file is a Jupyter notebook that performs an analysis of wind turbines in Texas (My location). Here's a breakdown of what's happening in the notebook:

1. **Loading and filtering data**: The notebook loads a shapefile containing the locations of wind turbines in the United States (Source: https://eerscmap.usgs.gov/uswtdb/). It then filters this data to only include turbines located in Texas.

2. **Visualizing the data**: The notebook uses the `pydeck` library to create a scatterplot layer of the wind turbines in Texas and displays this on a map.

3. **Filtering turbines built before 2012**: The notebook further filters the data to only include turbines built before 2012. It then visualizes this filtered data on a map.

4. **Clustering the data**: The notebook uses the DBSCAN algorithm from the `sklearn.cluster` library to identify clusters of wind turbines. It adds the cluster labels to the data and visualizes the clusters on a map, with different colors representing different clusters.

5. **Calculating cluster centroids**: Finally, the notebook calculates the centroid of each cluster (the average of the coordinates of all points in the cluster) and visualizes these centroids on the map.

### Streamlit Application

The `app.py` file is a Streamlit application for visualizing and analyzing wind speed data for wind turbines clusters in the United States.

1. **Imports**: The script imports necessary modules and classes, including Streamlit, pandas, and the `DataAnalysis` class from `src.data_analysis`.

2. **Streamlit Configuration**: The `set_page_config` function is used to set the page title and layout. Custom CSS is also added using the `st.markdown` function to style radio buttons.

3. **API Key and Email**: The script retrieves an API key and email from Streamlit secrets, which are used for data fetching in the `DataAnalysis` class.

4. **Title and Description**: The script sets the title and description of the Streamlit app using `st.title` and `st.write`.

5. **Data Loading**: The script loads a CSV file from a URL into a pandas DataFrame.

6. **Visualization Specification**: A visualization specification (`vis_spec`) is defined as a JSON string. This specification is used to configure the visualization of the data.

7. **Streamlit Renderer**: The `StreamlitRenderer` class from the `pygwalker.api.streamlit` module is used to create a Streamlit app for the data visualization.

8. **Data Analysis Option**: The script creates a radio button for the user to choose between viewing the data on a map ('Maps') or analyzing the data for a specific County in Texas ('Data').

9. **Data Analysis**: If the 'Data' option is selected, the script filters the DataFrame for the selected site, extracts the latitude and longitude, fetches the monthly wind data using the `DataAnalysis` class, and visualizes the data.

10. **Data Visualization**: The `StreamlitRenderer` class is used again to create a Streamlit app for the data visualization, this time using a different visualization specification (`vis_spec_data`).

11. **Explorer**: Finally, the `explorer` method of the `StreamlitRenderer` class is called to display the data explorer in the Streamlit app.