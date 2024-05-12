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

# Daily Analysis
df = DataAnalysis(31.9686, -99.9018, 2012, api_key, email).daily_data()

pyg_app = StreamlitRenderer(df)
 
pyg_app.explorer()
