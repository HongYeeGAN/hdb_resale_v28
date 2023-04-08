import streamlit as st
import pandas as pd

st.set_page_config(page_title="Forcasting")

st.markdown("<h4 style='color: #0066cc'>Estimate Future Price of Your Ideal Home</h4>", unsafe_allow_html=True)

st.markdown(
    """
    <div style='background-color: #0066cc; padding: 10px'>
        <h2 style='color: white;text-align: center;'>FORECASTING</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='background-color: white; padding: 10px'>
    </div>
    """,
    unsafe_allow_html=True
)


##### Change data source #####
### READ DATA ###
file_location = "updated_2017_to_now.csv"
data = pd.read_csv(file_location, index_col=0)
data = data.dropna(axis=0)
data = data.drop_duplicates().reset_index().drop("index", axis=1)

### SELECTIONS ###
# town

option_town = st.multiselect("Select a town", ("ANG MO KIO", "BEDOK", "BISHAN", "BUKIT BATOK", "BUKIT MERAH", "BUKIT PANJANG", "BUKIT TIMAH", "CENTRAL AREA","CHOA CHU KANG", "CLEMENTI", "GEYLANG", "HOUGANG", "JURONG EAST", "JURONG WEST", "KALLANG/WHAMPOA", "MARINE PARADE", "PASIR RIS", "PUNGGOL", "QUEENSTOWN", "SEMBAWANG", "SENGKANG", "SERANGOON", "TAMPINES", "TOA PAYOH", "WOODLANDS", "YISHUN"))
filtered_data = data[data["town"].isin(option_town)]

# flat type
filtered_flat = list(filtered_data["flat_type"].unique())
option_flat = st.selectbox("Select desired flat types", options=sorted(filtered_flat, key=str.lower))
filtered_data = filtered_data[filtered_data["flat_type"] == option_flat]





