from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
from src.data_analysis import DataAnalysis

st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

api_key = st.secrets['AUTH_TOKEN']
email = st.secrets['EMAIL']


# Create a dropdown menu for daily and monthly data
option = st.selectbox('Choose Data Analysis', ('Daily Data', 'Monthly Data'))

if option == 'Daily Data':
    df = DataAnalysis(31.9686, -99.9018, 2012, api_key, email).daily_data()
elif option == 'Monthly Data':
    df = DataAnalysis(31.9686, -99.9018, 2012, api_key, email).monthly_data()

pyg_app = StreamlitRenderer(df)
pyg_app.explorer()
