# Import necessary libraries and functions
import streamlit as st
from visuals import (plot_lga_presumptive_cases_trend, plot_lga_diagnosed_tb_cases_trend, 
                     show_choropleth_for_number_of_diagnosed, show_gender_age_tb_bar, 
                     kaduna_lgas, create_tb_cases_plot, create_tb_scatter_plot, 
                     plot_yearly_tb_cases, plot_quarterly_tb_cases, plot_total_lga_tb_cases)
from visuals import im

# Set page configuration
st.set_page_config(page_title="Kaduna Dashboard", 
                   layout="wide", 
                   initial_sidebar_state="auto",
                   page_icon=im)

# Set the title of the dashboard
st.header("Kaduna State Tuberculosis Dashboard", divider='grey')

# Introduction text
st.write("""
This interactive web application provides comprehensive insights into the Tuberculosis (TB) situation in Kaduna State, Nigeria. By leveraging data analytics and interactive visualizations, it enhances understanding and awareness of TB trends over the years.
Explore the prevalence of TB across various age groups, genders, and local government areas (LGAs) in Kaduna State. Analyze presumptive and diagnosed TB cases, track trends over time, and gain valuable insights into the distribution of cases within the region.
""")

# Display the overall TB cases plot
st.plotly_chart(create_tb_cases_plot(), use_container_width=True)

# Display the total LGA TB cases, yearly TB cases, and quarterly TB cases in a 3-column layout
column1, column2, column3 = st.columns(3)
column1.plotly_chart(plot_total_lga_tb_cases(), use_container_width=True)
column2.plotly_chart(plot_yearly_tb_cases(), use_container_width=True)
column3.plotly_chart(plot_quarterly_tb_cases(), use_container_width=True)

# Display the selected year and quarter
year_quarter_options = [
    '2019 Q1', '2019 Q2', '2019 Q3', '2019 Q4', '2020 Q1', '2020 Q2',
    '2020 Q3', '2020 Q4', '2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4',
    '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4', '2023 Q1', '2023 Q2',
    '2023 Q3', '2023 Q4']

st.markdown('---')

st.subheader('Quarterly Viewpoint')

st.write("""
This section provides a detailed analysis of TB cases on a quarterly basis. You can interactively select a year and quarter to visualize the data. The visualizations provide insights into 
the number of diagnosed cases, the distribution of cases by gender and age, and the clusters formed based TB cases activity.
""")

# Allow user to select a year and quarter
year_quarter = st.select_slider('Select Year and Quarter', options=year_quarter_options)

# Display the choropleth for number of diagnosed and gender-age TB bar in a 2-column layout
c1, c2 = st.columns(2)
c1.plotly_chart(show_choropleth_for_number_of_diagnosed(year_quarter), use_container_width=True)
c2.plotly_chart(show_gender_age_tb_bar(year_quarter), use_container_width=True)

# Display the scatter plot for the selected year and quarter
st.plotly_chart(create_tb_scatter_plot(year_quarter), use_container_width=True)

# st.subheader('Local Area Perspective')

# # Allow user to select a LGA
# lga_choice = st.selectbox('Select a Local Government Area (LGA)', kaduna_lgas)

# # Display the LGA presumptive cases trend and diagnosed TB cases trend in a 2-column layout
# c1_, c2_ = st.columns(2)
# c1_.plotly_chart(plot_lga_presumptive_cases_trend(lga_choice), use_container_width=True)
# c2_.plotly_chart(plot_lga_diagnosed_tb_cases_trend(lga_choice), use_container_width=True)