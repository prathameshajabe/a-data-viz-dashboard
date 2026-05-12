import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

df = pd.read_csv("india.csv")

list_of_states = list(df["State"].unique())
list_of_states.insert(0, "Overall")

st.sidebar.title("India's Data Visualization")

selected_state = st.sidebar.selectbox("select a state", list_of_states)
primary = st.sidebar.selectbox("select a primary state", sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("select a secondary state", sorted(df.columns[5:]))

plot = st.sidebar.button("plot Graph")

if plot:
    st.text("Size represents Primary parameter")
    st.text("Color represents Secondary parameter")
    if selected_state == "Overall":
        fig = px.scatter_mapbox(df, lat="Latitude", lon = "Longitude", size= primary, color= secondary, zoom = 4,size_max=35,
                                mapbox_style = "carto-positron", template = "plotly", width = 1200,height = 800, hover_name='District')

        st.plotly_chart(fig, use_container_width = True)
    else:
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6, size_max=35,
                                mapbox_style="carto-positron", template="plotly", width=1200, height=800,
                                hover_name='District')

        st.plotly_chart(fig, use_container_width=True)
