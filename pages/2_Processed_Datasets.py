import streamlit as st
import streamlit.components.v1 as components
from visuals import im
import pandas as pd

st.set_page_config(
    page_title="Processed TB",
    layout="wide",
    page_icon=im
)

# st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.image('images/omdena_kaduna.png', use_column_width="auto")

st.header("Kaduna Tuberculosis Datasets")

block1a_complete = pd.read_csv("datasets/block1a_19_to_23_complete.csv", index_col=0)
block2a_complete = pd.read_csv("datasets/block2a_19_to_23_complete.csv", index_col=0)
block2b_complete = pd.read_csv("datasets/block2b_19_to_23_complete.csv", index_col=0)
block2c_complete = pd.read_csv("datasets/block2c_19_to_23_complete.csv", index_col=0)
block2d_complete = pd.read_csv("datasets/block2d_19_to_23_complete.csv", index_col=0)
block2e_complete = pd.read_csv("datasets/block2e_19_to_23_complete.csv", index_col=0)

block_type = st.radio('Select a data block to load:',
                        options = ('block1a', 'block2a', 'block2b', 'block2c', 'block2d', 'block2e'),
                        horizontal = True)

st.radio()


with st.expander("Download the Datasets here"):

    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    
    st.subheader('Block 1a: Detailed Activities of Presumptive PTB Cases', divider='grey')
    st.caption("Data from 2019 to 2023")
    converted_block1a = convert_df(block1a_complete)
    
    st.download_button(
        label="Download block1a",
        data=converted_block1a,
        file_name='block1a_processed.csv',
        mime='text/csv',
    )
    
    st.subheader('Block 2a: Comprehensive Breakdown of All TB Cases', divider='grey')
    st.caption("Data from 2019 to 2023")
    converted_block2a = convert_df(block2a_complete)
    
    st.download_button(
        label="Download block2a",
        data=converted_block2a,
        file_name='block2a_processed.csv',
        mime='text/csv',
    )
    
    st.subheader('Block 2b: Demographic Breakdown of All TB Cases (by Sex and Age Group)', divider='grey')
    st.caption("Data from 2019 to 2023")
    converted_block2b = convert_df(block2b_complete)
    
    st.download_button(
        label="Download block2b",
        data=converted_block2b,
        file_name='block2b_processed.csv',
        mime='text/csv',
    )
    
    st.subheader('Block 2c: Demographic Breakdown of New and Relapse TB Cases (by Sex and Age Group)', divider='grey')
    st.caption("Data from 2019 to 2023")
    converted_block2c = convert_df(block2c_complete)
    
    st.download_button(
        label="Download block2c",
        data=converted_block2c,
        file_name='block2c_processed.csv',
        mime='text/csv',
    )
    
    st.subheader('Block 2d: Demographic Breakdown of HIV-Positive TB Cases (by Sex and Age Group)', divider='grey')
    st.caption("Data from 2019 to 2023")
    converted_block2d = convert_df(block2d_complete)
    
    st.download_button(
        label="Download block2d",
        data=converted_block2d,
        file_name='block2d_processed.csv',
        mime='text/csv',
    )
    
    st.subheader('Block 2e: Demographic Breakdown of HIV-Positive TB Cases (by Sex and Case Category)', divider='grey')
    st.caption("Data from 2019 to 2023")
    converted_block2e = convert_df(block2e_complete)
    
    st.download_button(
        label="Download block2e",
        data=converted_block2e,
        file_name='block2e_processed.csv',
        mime='text/csv',
    )



