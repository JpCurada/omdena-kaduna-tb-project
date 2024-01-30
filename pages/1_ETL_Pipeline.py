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

Transformed Data

- **Block1a:** Detailed Activities of Presumptive PTB Cases

- **Block2a** Comprehensive Breakdown of All TB Cases
         
- **Block2b:** Demographic Breakdown of All TB Cases (by Sex and Age Group)
         
- **Block2c:** Demographic Breakdown of New and Relapse TB Cases (by Sex and Age Group)
         
- **Block2d:** Demographic Breakdown of HIV-Positive TB Cases (by Sex and Age Group)

- **Block2e:** Demographic Breakdown of HIV-Positive TB Cases (by Sex and Case Category)

""")

st.markdown('---')

st.write("Click [raw data](https://drive.google.com/drive/folders/1qeHsngqf-2UQ4uaycoE2ubc1BcBnocy0) to get the data you can try with the ETL pipeline.")

col1, col2, col3 = st.columns(3)
block_type = col1.radio('Select a data block to process:',
                        options = ('block1a', 'block2a', 'block2b', 'block2c', 'block2d', 'block2e'),
                        horizontal = True)
year_choice = col2.number_input('Year of the recorded data:', placeholder="Ex. `2023` then Press `Enter`", min_value=2019, step=1)

excel_file = col3.file_uploader("Choose a file", type = 'xlsx')

if excel_file is not None and block_type is not None and year_choice is not None:
    with st.spinner('Processing...'):
        try:
            processed_data = process_lga_data(block_type, excel_file, year_choice)
            
        except (KeyError, ValueError) as e:
            st.error(f"Error: The uploaded Excel file does not adhere to the expected structure "
                     "for 2023 TB cases. Please refer to the [2023 TB Cases Excel File](https://drive.google.com/drive/folders/1qeHsngqf-2UQ4uaycoE2ubc1BcBnocy0) "
                     "for proper formatting. If you need assistance, contact the team. 🚨")

             # st.dataframe has a default comma in its values, to remove it:
            s = processed_data.style.format({"Year": lambda x: '{:.0f}'.format(x)})
            # Display the formatted dataframe
            st.subheader(f"{data_desc[block_type]}", divider='grey')
            st.dataframe(s)
          
            st.subheader(f"Load and Explore the Transformed {block_type}", divider='grey')
            st.write("""
            Load and explore the transformed data block using Pygwalker. This interactive exploration 
            interface allows us to build charts by simply dragging and dropping the desired fields. 
            This hands-on approach facilitates a deeper understanding of the data and aids in the 
            discovery of valuable insights. 
            For more information on how to use Pygwalker, please refer to the official 
            [guides on visualizing](https://docs.kanaries.net/graphic-walker/data-viz/create-data-viz).
            """)

            # Generate the HTML using Pygwalker
            pyg_html = pyg.to_html(processed_data)

            # Embed the HTML into the Streamlit app
            components.html(pyg_html, height=1000, scrolling=True)


