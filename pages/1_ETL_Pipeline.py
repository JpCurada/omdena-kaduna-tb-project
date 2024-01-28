import streamlit as st
from etl import process_lga_data
import streamlit.components.v1 as components
import pygwalker as pyg
from visuals import im

st.set_page_config(page_title="Kaduna TB Explorer", 
                   page_icon=im, 
                   layout="wide", 
                   initial_sidebar_state="auto", 
                   menu_items=None)


st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.header("ETL Pipeline for Kaduna LGAs TB Data", divider='grey')

data_desc = {
    'block1a':'Detailed Activities of Presumptive PTB Cases',
    'block2a':'Comprehensive Breakdown of All TB Cases',
    'block2b':'Demographic Breakdown of All TB Cases (by Sex and Age Group)',
    'block2c':'Demographic Breakdown of New and Relapse TB Cases (by Sex and Age Group)',
    'block2e':'Demographic Breakdown of HIV-Positive TB Cases (by Sex and Age Group)'
}

st.write("""

This section is dedicated to the Python program that performs an Extract, Transform, Load (ETL) process on the Standard Excel dataset of Tuberculosis (TB) cases in Kaduna. The dataset is structured with multiple sheets, each representing data for a specific Local Government Area (LGA).

The ETL process implemented here serves two main purposes:

- **Extract:** The code reads data from an Excel file, extracting information from multiple sheets within the file. Each sheet corresponds to a specific LGA.

- **Transform:** The extracted data is then transformed. This involves selecting specific rows and columns, inserting new data, renaming columns, and preparing the data in a format that is suitable for further analysis or processing.

- **Load:** Finally, the transformed data is loaded into a pandas DataFrame. This DataFrame can be used for further data analysis tasks or can be saved in a different format like CSV for other uses.

This section is an essential part of our data preprocessing pipeline, turning raw, multi-sheet Excel data into a clean, single-table format that’s easier to work with for downstream tasks such as data analysis and machine learning. By automating this process in a Streamlit application, we ensure that our data preprocessing is reproducible and consistent, saving us time and reducing the potential for manual errors. 

Transformed Data

- **Block1a:** Detailed Activities of Presumptive PTB Cases

- **Block2a** Comprehensive Breakdown of All TB Cases
         
- **Block2b:** Demographic Breakdown of All TB Cases (by Sex and Age Group)
         
- **Block2c:** Demographic Breakdown of New and Relapse TB Cases (by Sex and Age Group)
         
- **Block2d:** Demographic Breakdown of HIV-Positive TB Cases (by Sex and Age Group)

- **Block2e:** Demographic Breakdown of HIV-Positive TB Cases (by Sex and Case Category)
                      
""")

st.markdown('---')

col1, col2, col3 = st.columns(3)
block_type = col1.radio('Select a data block to process:',
                        options = ('block1a', 'block2a', 'block2b', 'block2c', 'block2d', 'block2e'),
                        horizontal = True)
year_choice = col2.number_input('Year of the recorded data:', placeholder="Ex. `2023` then Press `Enter`", step=1)

excel_file = col3.file_uploader("Choose a file", type = 'xlsx')

if excel_file is not None and block_type is not None and year_choice is not None:
    with st.spinner('Processing...'):
        processed_data = process_lga_data(block_type, excel_file, year_choice)
        # st.dataframe has a default comma in their values, to remove it:
        s = processed_data.style.format({"Year": lambda x : '{:.0f}'.format(x)})
        # Display the dataframe with formatted numeric columns
        st.subheader(f"{data_desc[block_type]}", divider='grey')
        st.dataframe(s)

        st.subheader(f"Load and Explore the Transformed {block_type}", divider='grey')
        st.write("""
        Load and explore the transformed data block using Pygwalker. This interactive exploration 
        interface allows us to build charts by simply dragging and dropping the desired fields. 
        This hands-on approach facilitates a deeper understanding of the data and aids in the 
        discovery of valuable insights. 
        For more information on how to use Pygwalker, please refer to the official [guides on visualizing](https://docs.kanaries.net/graphic-walker/data-viz/create-data-viz).
        """)

        # Generate the HTML using Pygwalker
        pyg_html = pyg.to_html(processed_data)

        # Embed the HTML into the Streamlit app
        components.html(pyg_html, height=1000, scrolling=True)
 
