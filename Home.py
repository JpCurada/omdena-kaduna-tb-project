import streamlit as st
import streamlit.components.v1 as components
from visuals import im

st.set_page_config(
    page_title="Kaduna TB Explorer",
    layout="wide",
    page_icon=im
)

st.image('images/omdena_kaduna.png', use_column_width="auto")

st.header("Kaduna TB Explorer: ETL Pipeline")



