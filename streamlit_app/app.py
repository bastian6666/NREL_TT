from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
from src.data_analysis import DataAnalysis
import os

st.set_page_config(
    page_title="Wind Speed Data Analysis",
    layout="wide"
)

st.markdown("""
<style>
div.row-widget.stRadio > div {
    display: flex;
    flex-direction: row;
    justify-content: start;
}
label[data-baseweb="radio"] {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin: 5px 10px;
    padding: 8px 16px;  # Adjust padding for better text fit
    background-color: #0078D4;  # A nicer shade of blue
    border: 2px solid #0053A0;  # A darker blue for the border
    border-radius: 20px;  # Rounded corners
    color: white;  # White text color
    font-family: sans-serif;  # Improve the font style
    font-size: 16px;  # Larger font size for better readability
}
label[data-baseweb="radio"]:hover {
    background-color: #0053A0;  # Darker blue on hover for better interaction feedback
}
label[data-baseweb="radio"] input {
    display: none;  # Hide the default radio button
}
</style>
""", unsafe_allow_html=True)

api_key = st.secrets['AUTH_TOKEN']
email = st.secrets['EMAIL']

# Title
st.title('Wind Speed Data Analysis')

# Description
st.write('This app allows you to visualize wind speed data for wind turbines clusters in the United States. You can choose to view the data on a map or analyze the data for a specific County in Texas.')

# Load the data
url = "https://raw.githubusercontent.com/bastian6666/NREL_TT/main/streamlit_app/app_data/clusters.csv"

df_map = pd.read_csv(url)
vis_spec = """{"config":[{"config":{"defaultAggregated":false,"geoms":["poi"],"coordSystem":"geographic","limit":-1,"timezoneDisplayOffset":0},"encodings":{"dimensions":[{"fid":"faa_ors","name":"faa_ors","basename":"faa_ors","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_state","name":"t_state","basename":"t_state","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_county","name":"t_county","basename":"t_county","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_fips","name":"t_fips","basename":"t_fips","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"p_name","name":"p_name","basename":"p_name","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_manu","name":"t_manu","basename":"t_manu","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_model","name":"t_model","basename":"t_model","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_img_date","name":"t_img_date","basename":"t_img_date","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_img_srce","name":"t_img_srce","basename":"t_img_srce","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"geometry","name":"geometry","basename":"geometry","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"cluster_label","name":"cluster_label","basename":"cluster_label","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"geometry_centroid","name":"geometry_centroid","basename":"geometry_centroid","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"fid":"case_id","name":"case_id","basename":"case_id","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"faa_asn","name":"faa_asn","basename":"faa_asn","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"usgs_pr_id","name":"usgs_pr_id","basename":"usgs_pr_id","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"eia_id","name":"eia_id","basename":"eia_id","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"p_year","name":"p_year","basename":"p_year","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"p_tnum","name":"p_tnum","basename":"p_tnum","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"p_cap","name":"p_cap","basename":"p_cap","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_cap","name":"t_cap","basename":"t_cap","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_hh","name":"t_hh","basename":"t_hh","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_rd","name":"t_rd","basename":"t_rd","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_rsa","name":"t_rsa","basename":"t_rsa","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_ttlh","name":"t_ttlh","basename":"t_ttlh","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"offshore","name":"offshore","basename":"offshore","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"retrofit","name":"retrofit","basename":"retrofit","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"retrofit_y","name":"retrofit_y","basename":"retrofit_y","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_conf_atr","name":"t_conf_atr","basename":"t_conf_atr","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_conf_loc","name":"t_conf_loc","basename":"t_conf_loc","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"xlong","name":"xlong","basename":"xlong","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"ylat","name":"ylat","basename":"ylat","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"xlong_centroid","name":"xlong_centroid","basename":"xlong_centroid","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"ylat_centroid","name":"ylat_centroid","basename":"ylat_centroid","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[{"fid":"ylat","name":"ylat","basename":"ylat","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0}],"columns":[{"fid":"xlong","name":"xlong","basename":"xlong","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0}],"color":[{"fid":"p_cap","name":"p_cap","basename":"p_cap","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0}],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[{"fid":"xlong","name":"xlong","basename":"xlong","analyticType":"dimension","semanticType":"quantitative","aggName":"sum","offset":0}],"latitude":[{"fid":"ylat","name":"ylat","basename":"ylat","analyticType":"dimension","semanticType":"quantitative","aggName":"sum","offset":0}],"geoId":[],"details":[{"fid":"p_year","name":"p_year","basename":"p_year","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"faa_asn","name":"faa_asn","basename":"faa_asn","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"case_id","name":"case_id","basename":"case_id","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0}],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"full","width":800,"height":600},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false}},"visId":"gw_Z4XL","name":"Wind Turbines"},{"config":{"defaultAggregated":false,"geoms":["poi"],"coordSystem":"geographic","limit":-1,"timezoneDisplayOffset":0},"encodings":{"dimensions":[{"fid":"faa_ors","name":"faa_ors","basename":"faa_ors","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_state","name":"t_state","basename":"t_state","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_county","name":"t_county","basename":"t_county","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_fips","name":"t_fips","basename":"t_fips","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"p_name","name":"p_name","basename":"p_name","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_manu","name":"t_manu","basename":"t_manu","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_model","name":"t_model","basename":"t_model","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_img_date","name":"t_img_date","basename":"t_img_date","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"t_img_srce","name":"t_img_srce","basename":"t_img_srce","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"geometry","name":"geometry","basename":"geometry","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"cluster_label","name":"cluster_label","basename":"cluster_label","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"geometry_centroid","name":"geometry_centroid","basename":"geometry_centroid","semanticType":"ordinal","analyticType":"dimension","offset":0},{"fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"fid":"case_id","name":"case_id","basename":"case_id","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"faa_asn","name":"faa_asn","basename":"faa_asn","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"usgs_pr_id","name":"usgs_pr_id","basename":"usgs_pr_id","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"eia_id","name":"eia_id","basename":"eia_id","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"p_year","name":"p_year","basename":"p_year","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"p_tnum","name":"p_tnum","basename":"p_tnum","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"p_cap","name":"p_cap","basename":"p_cap","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_cap","name":"t_cap","basename":"t_cap","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_hh","name":"t_hh","basename":"t_hh","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_rd","name":"t_rd","basename":"t_rd","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_rsa","name":"t_rsa","basename":"t_rsa","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_ttlh","name":"t_ttlh","basename":"t_ttlh","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"offshore","name":"offshore","basename":"offshore","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"retrofit","name":"retrofit","basename":"retrofit","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"retrofit_y","name":"retrofit_y","basename":"retrofit_y","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_conf_atr","name":"t_conf_atr","basename":"t_conf_atr","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"t_conf_loc","name":"t_conf_loc","basename":"t_conf_loc","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"xlong","name":"xlong","basename":"xlong","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"ylat","name":"ylat","basename":"ylat","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"xlong_centroid","name":"xlong_centroid","basename":"xlong_centroid","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"ylat_centroid","name":"ylat_centroid","basename":"ylat_centroid","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[],"columns":[],"color":[{"fid":"t_county","name":"t_county","basename":"t_county","semanticType":"nominal","analyticType":"dimension","offset":0}],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[{"fid":"xlong_centroid","name":"xlong_centroid","basename":"xlong_centroid","analyticType":"dimension","semanticType":"quantitative","aggName":"sum","offset":0}],"latitude":[{"fid":"ylat_centroid","name":"ylat_centroid","basename":"ylat_centroid","analyticType":"dimension","semanticType":"quantitative","aggName":"sum","offset":0}],"geoId":[],"details":[],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"full","width":800,"height":600},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false}},"visId":"gw_8sHo","name":"Cluster Centroids"}],"chart_map":{},"workflow_list":[{"workflow":[{"type":"view","query":[{"op":"raw","fields":["xlong","ylat","p_cap","p_year","faa_asn","case_id"]}]}]},{"workflow":[{"type":"view","query":[{"op":"raw","fields":["xlong_centroid","ylat_centroid","t_county"]}]}]}],"version":"0.4.8.3"}"""
pyg_app = StreamlitRenderer(df_map, spec = vis_spec)
# Create a dropdown menu for daily and monthly data
option = st.radio(
    "Choose Data Analysis",
    ('Maps', 'Data')
)


if option == 'Data':
    df_unique = df_map.drop_duplicates(subset=['ylat_centroid'])

    site_list = df_unique['t_county'].tolist()
    site_options = st.selectbox('Select Site:', site_list) 

    # Display the selected site's coordinates
    selected_site = df_map[df_map['t_county'] == site_options]  # Filter the DataFrame for the selected site
    latitude = selected_site['ylat_centroid'].values[0]  # Extract latitude
    longitude = selected_site['xlong_centroid'].values[0]  # Extract longitude
    df = DataAnalysis(latitude, longitude, 2012, api_key, email).monthly_data()
    vis_spec_data = """{"config":[{"config":{"defaultAggregated":false,"geoms":["circle"],"coordSystem":"generic","limit":-1,"timezoneDisplayOffset":0},"encodings":{"dimensions":[{"fid":"Month","name":"Month","basename":"Month","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"fid":"Day","name":"Day","basename":"Day","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"Year","name":"Year","basename":"Year","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"Hour","name":"Hour","basename":"Hour","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"Minute","name":"Minute","basename":"Minute","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 10m (m/s)","name":"wind speed at 10m (m/s)","basename":"wind speed at 10m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 60m (m/s)","name":"wind speed at 60m (m/s)","basename":"wind speed at 60m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 100m (m/s)","name":"wind speed at 100m (m/s)","basename":"wind speed at 100m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 140m (m/s)","name":"wind speed at 140m (m/s)","basename":"wind speed at 140m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 200m (m/s)","name":"wind speed at 200m (m/s)","basename":"wind speed at 200m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[{"fid":"wind speed at 10m (m/s)","name":"wind speed at 10m (m/s)","basename":"wind speed at 10m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 60m (m/s)","name":"wind speed at 60m (m/s)","basename":"wind speed at 60m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 100m (m/s)","name":"wind speed at 100m (m/s)","basename":"wind speed at 100m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 140m (m/s)","name":"wind speed at 140m (m/s)","basename":"wind speed at 140m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 200m (m/s)","name":"wind speed at 200m (m/s)","basename":"wind speed at 200m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0}],"columns":[{"fid":"Month","name":"Month","basename":"Month","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"Day","name":"Day","basename":"Day","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0}],"color":[{"fid":"wind speed at 200m (m/s)","name":"wind speed at 200m (m/s)","basename":"wind speed at 200m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0}],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[],"latitude":[],"geoId":[],"details":[],"filters":[{"fid":"Month","name":"Month","basename":"Month","semanticType":"quantitative","analyticType":"dimension","offset":0,"rule":{"type":"range","value":[1,12]}}],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"auto","width":1351,"height":588},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false},"scaleIncludeUnmatchedChoropleth":false,"showAllGeoshapeInChoropleth":false,"colorPalette":"redblue","useSvg":false,"scale":{"opacity":{},"size":{}}},"visId":"gw_s2BP","name":"Daily Visualization"},{"config":{"defaultAggregated":true,"geoms":["bar"],"coordSystem":"generic","limit":-1,"timezoneDisplayOffset":0},"encodings":{"dimensions":[{"fid":"Month","name":"Month","basename":"Month","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"fid":"Day","name":"Day","basename":"Day","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"Year","name":"Year","basename":"Year","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"Hour","name":"Hour","basename":"Hour","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"Minute","name":"Minute","basename":"Minute","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 10m (m/s)","name":"wind speed at 10m (m/s)","basename":"wind speed at 10m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 60m (m/s)","name":"wind speed at 60m (m/s)","basename":"wind speed at 60m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 100m (m/s)","name":"wind speed at 100m (m/s)","basename":"wind speed at 100m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 140m (m/s)","name":"wind speed at 140m (m/s)","basename":"wind speed at 140m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"wind speed at 200m (m/s)","name":"wind speed at 200m (m/s)","basename":"wind speed at 200m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[{"fid":"wind speed at 10m (m/s)","name":"wind speed at 10m (m/s)","basename":"wind speed at 10m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"mean","offset":0},{"fid":"wind speed at 60m (m/s)","name":"wind speed at 60m (m/s)","basename":"wind speed at 60m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"mean","offset":0},{"fid":"wind speed at 100m (m/s)","name":"wind speed at 100m (m/s)","basename":"wind speed at 100m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"mean","offset":0},{"fid":"wind speed at 140m (m/s)","name":"wind speed at 140m (m/s)","basename":"wind speed at 140m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"mean","offset":0},{"fid":"wind speed at 200m (m/s)","name":"wind speed at 200m (m/s)","basename":"wind speed at 200m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"mean","offset":0}],"columns":[{"fid":"Month","name":"Month","basename":"Month","semanticType":"quantitative","analyticType":"dimension","offset":0}],"color":[{"fid":"wind speed at 200m (m/s)","name":"wind speed at 200m (m/s)","basename":"wind speed at 200m (m/s)","analyticType":"measure","semanticType":"quantitative","aggName":"mean","offset":0}],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[],"latitude":[],"geoId":[],"details":[],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"fixed","width":1000,"height":1000},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false},"scaleIncludeUnmatchedChoropleth":false,"showAllGeoshapeInChoropleth":false,"colorPalette":"redblue","useSvg":false,"scale":{"opacity":{},"size":{}},"primaryColor":"rgba(0,208,132,1)"},"visId":"gw_Svu4","name":"Monthly Visualization"}],"chart_map":{},"workflow_list":[{"workflow":[{"type":"filter","filters":[{"fid":"Month","rule":{"type":"range","value":[1,12]}}]},{"type":"view","query":[{"op":"raw","fields":["Month","Day","wind speed at 10m (m/s)","wind speed at 60m (m/s)","wind speed at 100m (m/s)","wind speed at 140m (m/s)","wind speed at 200m (m/s)","wind speed at 200m (m/s)"]}]}]},{"workflow":[{"type":"view","query":[{"op":"aggregate","groupBy":["Month"],"measures":[{"field":"wind speed at 10m (m/s)","agg":"mean","asFieldKey":"wind speed at 10m (m/s)_mean"},{"field":"wind speed at 60m (m/s)","agg":"mean","asFieldKey":"wind speed at 60m (m/s)_mean"},{"field":"wind speed at 100m (m/s)","agg":"mean","asFieldKey":"wind speed at 100m (m/s)_mean"},{"field":"wind speed at 140m (m/s)","agg":"mean","asFieldKey":"wind speed at 140m (m/s)_mean"},{"field":"wind speed at 200m (m/s)","agg":"mean","asFieldKey":"wind speed at 200m (m/s)_mean"}]}]}]}],"version":"0.4.8.3"}"""
    pyg_app = StreamlitRenderer(df, spec = vis_spec_data)


pyg_app.explorer()
