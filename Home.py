import streamlit as st
import streamlit.components.v1 as components
from visuals import im

st.set_page_config(
    page_title="Kaduna TB Explorer",
    layout="wide",
    page_icon=im
)

st.image('images/omdena_kaduna.png', use_column_width="auto")

st.header("Kaduna TB Explorer: A Data Science Approach to Tuberculosis Analysis")

st.subheader('Challenge Background', divider='grey')
st.write("""
         Tuberculosis (TB) is often underestimated by the general public, 
         despite being a significant health risk. As a communicable disease, 
         it can easily spread from person to person. Recognizing its impact, 
         the Sustainable Development Goals (SDGs) classify TB alongside HIV and 
         Malaria as an epidemic. The Nigerian Government’s National Tuberculosis 
         and Leprosy Control Programme (NTBLCP) Strategic Plan 2021–2025 aims to 
         end the TB epidemic in Nigeria by ensuring all Nigerians have access to 
         comprehensive, high-quality, patient-centered, and community-owned TB services.
         """)

st.subheader('The Problem', divider='grey')
st.write("""
            This project seeks to automate the analysis of state-collected 
         and compiled data using data science. The goal is to present insightful 
         visualizations of the data through an interactive tool.
         """)

st.subheader('Goal of the Project', divider='grey')
st.write("""
            Our objective is to address the irregularities in the community-collected data 
         by cleaning, pre-processing, and exploring available TB data in Kaduna State from 
         2019 to the most recent quarter of 2023. We aim to create a tool that health service 
         providers can use to make informed decisions about TB in Kaduna State. We also 
         strive to foster a strong relationship with the state agency responsible for 
         monitoring TB. Lastly, we aim to develop an interactive tool for analyzing the 
         collected data each quarter. This tool will present the data comprehensively, 
         allowing for logical and factual deductions and visualizations.
         """)




