import streamlit as st
import streamlit.components.v1 as components
from visuals import im
import pandas as pd

st.set_page_config(
    page_title="Processed TB",
    layout="wide",
    page_icon=im
)

st.image('images/omdena_kaduna.png', use_column_width="auto")

st.header("Kaduna Tuberculosis Datasets")

st.subheader('Block 1a: Detailed Activities of Presumptive PTB Cases', divider='grey')
st.caption("Data from 2019 to 2023")

block1a_complete = pd.read_csv("datasets/block1a_19_to_23_complete.csv")
st.download_button(
    label="Download block1a",
    data=block1a_complete,
    file_name='block1a_processed.csv',
    mime='text/csv',
)

st.subheader('Block 2a: Comprehensive Breakdown of All TB Cases', divider='grey')
st.caption("Data from 2019 to 2023")

block2a_complete = pd.read_csv("datasets/block2a_19_to_23_complete.csv")
st.download_button(
    label="Download block2a",
    data=block2a_complete,
    file_name='block2a_processed.csv',
    mime='text/csv',
)

st.subheader('Block 2b: Demographic Breakdown of All TB Cases (by Sex and Age Group)', divider='grey')
st.caption("Data from 2019 to 2023")

block2b_complete = pd.read_csv("datasets/block2b_19_to_23_complete.csv")
st.download_button(
    label="Download block2b",
    data=block2b_complete,
    file_name='block2b_processed.csv',
    mime='text/csv',
)

st.subheader('Block 2c: Demographic Breakdown of New and Relapse TB Cases (by Sex and Age Group)', divider='grey')
st.caption("Data from 2019 to 2023")

block2c_complete = pd.read_csv("datasets/block2c_19_to_23_complete.csv")
st.download_button(
    label="Download block2c",
    data=block2c_complete,
    file_name='block2c_processed.csv',
    mime='text/csv',
)

st.subheader('Block 2d: Demographic Breakdown of HIV-Positive TB Cases (by Sex and Age Group)', divider='grey')
st.caption("Data from 2019 to 2023")

block2d_complete = pd.read_csv("datasets/block2d_19_to_23_complete.csv")
st.download_button(
    label="Download block2d",
    data=block2d_complete,
    file_name='block2d_processed.csv',
    mime='text/csv',
)

