import numpy as np
import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
im = Image.open("images/omdena_kaduna_chapter_logo.png")

block1a = pd.read_csv("datasets/block1a_19_to_23_complete.csv", index_col=0)
block2a = pd.read_csv("datasets/block2a_19_to_23_complete.csv", index_col=0)
block2b =  pd.read_csv("datasets/block2b_19_to_23_complete.csv")
tb_cluster = pd.read_csv("datasets/block2a_for_clustering_19_to_23_complete_4_clusters.csv")

# Read the shapefile
shapes = gpd.read_file("./nga_adm_osgof_20190417/nga_admbnda_adm2_osgof_20190417.shp")
c_lat = 10.3764
c_lon = 7.7095
geodf = block2a.merge(shapes, left_on='LGA', right_on='ADM2_EN', how='left')
geodf = gpd.GeoDataFrame(geodf)


# Forecasted df
grouped_df = pd.read_csv("datasets/total_tb_notified_with_predicted.csv")

kaduna_lgas = block1a['LGA'].unique()

def plot_lga_presumptive_cases_trend(lga_name):
    """
    Generates and displays a line chart showing the trend in presumptive cases
    for a specific LGA over time.

    Args:
        lga_name: The name of the LGA to analyze.

    Returns:
        A Plotly Express figure object representing the line chart.
    """

    # Filter data for the chosen LGA
    lga_data = block1a[block1a["LGA"] == lga_name]

    # Generate the line chart with Plotly Express
    fig = px.line(
        lga_data,
        x="Year_Quarter",
        y="Total number of presumptives",
        markers=True,
        line_shape="linear",
        title=f"Presumptive Cases Trend in {lga_name}<br><sup>Data from 2019 to 2023 of block1a</sup>",
    )

    # Customize the chart layout for clarity
    fig.update_layout(
        xaxis_title="Year and Quarter",
        yaxis_title="Number of Presumptives",
    )

    return fig


def plot_lga_diagnosed_tb_cases_trend(lga_name):
    """
    Generates and displays a line chart showing the trend in diagnosed tuberculosis (TB) cases
    for a specific Local Government Area (LGA) over time.

    Args:
        lga_name: The name of the LGA to analyze.

    Returns:
        A Plotly Express figure object representing the line chart.
    """

    # Filter data for the chosen LGA
    lga_data = block2a[block2a["LGA"] == lga_name]

    # Generate the line chart with Plotly Express
    fig = px.line(
        lga_data,
        x="Year-Quarter",
        y="Total TB Cases notified",  # Rename "Total diagnosed" to be consistent with overall data frame
        markers=True,
        line_shape="linear",
        title=f"What is the Trend of Confirmed TB Cases in {lga_name}?<br><sup>Data from 2019 to 2023 of block2a</sup>",
    )

    # Customize the chart layout for clarity
    fig.update_layout(
        xaxis_title="Year and Quarter",
        yaxis_title="Total TB Cases notified",  # Rename y-axis title to match variable name
    )

    return fig


def show_choropleth_for_number_of_diagnosed(year_quarter):
    # Filter the GeoDataFrame for the specified year_quarter
    sliced_geodf = geodf[geodf['Year-Quarter'] == year_quarter]

    # Create a choropleth map using Plotly Express
    choropleth_fig = px.choropleth(
        sliced_geodf,
        geojson=sliced_geodf.geometry,
        locations=sliced_geodf.index,
        color='Total TB Cases notified',
        hover_name='ADM2_EN',
        color_continuous_scale='PuBu',
        projection="mercator",
        labels='Total TB Cases notified',
        custom_data=['ADM2_EN', 'Total TB Cases notified'],  # Custom data for tooltip
        title=f"How many TB Cases were notified in each LGA for {year_quarter}? <br><sup>Data from 2019 to 2023 of block2a</sup>"
    )

    # Customize the hover template to show LGA and number of diagnosed
    choropleth_fig.update_traces(
        hovertemplate="<b>%{customdata[0]}</b><br>Diagnosed: %{customdata[1]:,}<extra></extra>"
    )

    # Adjust layout settings
    choropleth_fig.update_layout(autosize=False, width=800, height=600)
    choropleth_fig.update_geos(fitbounds="locations", visible=False)

    return choropleth_fig

def show_gender_age_tb_bar(year_quarter):
    """
    Generates and displays a grouped bar chart showing the distribution of age groups by gender.

    Args:
        year_quarter (str): The year and quarter for which the data is visualized.

    Returns:
        A Plotly Express figure object representing the grouped bar chart.
    """
    # Melt the DataFrame to transform it into a suitable format for Plotly Express
    melted_df = pd.melt(
        block2b,
        id_vars=['Year_Quarter', 'LGA', 'Sex'],
        value_vars=['0-4', '5-14', '15-24', '25-34', '35-44', '45-54', '55-64'],
        var_name='Age_Group',
        value_name='Values'
    )

    # Sum the values grouped by year_quarter, age_group, and sex
    aggregated_df = melted_df.groupby(["Year_Quarter", "Age_Group", "Sex"], as_index=False)['Values'].sum()

    # Filter data for the specified year_quarter
    filtered_df = aggregated_df[aggregated_df["Year_Quarter"] == year_quarter]

    # Create the grouped bar chart
    chart_title = f"For which sex and age group were the most TB cases reported in {year_quarter}?<br><sup>Data Source: block2b</sup>"
    fig = px.bar(
        filtered_df,
        x='Age_Group',
        y='Values',
        color='Sex',
        barmode='group',
        title=chart_title,
    )

    # Customize the layout
    fig.update_layout(
        xaxis_title='Age Group',
        yaxis_title='Count',
        height=600,
        width=1200
    )

    return fig

def create_tb_cases_plot():
    fig = go.Figure()

    # Full line for all years
    fig.add_scattergl(x=grouped_df['Year_Quarter_'], 
                      y=grouped_df['Total TB Cases notified Actual and Forecast'], 
                      line={'color': 'blue'},
                      showlegend=False)  # Set showlegend to False

    # Above threshold line for the year 2024
    fig.add_scattergl(x=grouped_df['Year_Quarter_'][grouped_df['Year_Quarter_'].str.split(" ", expand=True)[0] == '2024'], 
                      y=grouped_df['Total TB Cases notified Actual and Forecast'][grouped_df['Year_Quarter_'].str.split(" ", expand=True)[0] == '2024'], 
                      line={'color': 'red'},
                      showlegend=False)  # Set showlegend to False

    # Customize the layout
    fig.update_layout(title='What is the Projection of Total TB Cases for Kaduna State in 2024?',
                      xaxis_title='Year and Quarter',
                      yaxis_title='Total TB Cases')

    return fig

def create_tb_scatter_plot(year_quarter):
    # Filter data for the specified year and quarter
    filtered_data = tb_cluster[tb_cluster['Year_Quarter'] == year_quarter]

    # Create scatter plot using Plotly Express
    fig = px.scatter(filtered_data, x='PTB Cases', y='EPTB Cases', color="Cluster", size="Total TB Cases notified", hover_data=['LGA'],
                     title=f'Which LGAs Showed the Most TB Activity in {year_quarter}?<br><sup>Cluster 1: No EPTB Cases         Cluster 2: 1 EPTB Case       Cluster 3: Moderate PTB & EPTB Cases        Cluster 4: High PTB & High EPTB </sup>',
                     labels={'EPTB Cases': 'EPTB Cases', 'Total TB Cases notified': 'Total TB Cases', 'PTB Cases': 'PTB Cases'},
                     color_continuous_scale='viridis',
                     size_max=30,
                     )





    fig.update_layout(coloraxis_showscale=False)

    # Show the plot
    return fig

def plot_quarterly_tb_cases():

    quarterly_tb_cases = block2a.groupby('Quarter', as_index=False)['Total TB Cases notified'].sum()

    # Generate the bar chart with Plotly Express
    fig = px.bar(
        quarterly_tb_cases,
        x="Quarter",
        y="Total TB Cases notified",
        title=f"How many TB cases occur per quarter?<br><sup>Data from 2019 to 2023 of block2a</sup>",
        labels={"Total TB Cases notified": "Total Cases"},
    )

    # Customize the chart layout for clarity
    fig.update_layout(
        xaxis_title="Quarter",
        yaxis_title="Total TB Cases notified",
        showlegend=False,  # If you don't need a legend
    )

    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = [1, 2, 3, 4],
            ticktext = [1, 2, 3, 4]
        )
    )

    return fig

def plot_total_lga_tb_cases():
   """
   Calculates and plots the total TB cases notified for each LGA,
   highlighting those with the highest recorded cases.
   """

   # Calculate total TB cases per LGA, sort in descending order, and get the top 5
   total_tb_cases_per_lga = block2a.groupby('LGA', as_index=False)['Total TB Cases notified'].sum()
   top5_lga_tb_cases = total_tb_cases_per_lga.nlargest(5, 'Total TB Cases notified').sort_values(by='Total TB Cases notified', ascending=True)


   # Create the horizontal bar chart with Plotly Express
   fig = px.bar(
       top5_lga_tb_cases,
       y="LGA",
       x="Total TB Cases notified",
       title="Which LGAs Have the Highest Recorded TB Cases?<br><sup>Data from 2019 to 2023 of block2a</sup>",
       labels={"Total TB Cases notified": "Total Cases"},
       orientation="h",  # Set orientation to horizontal
   )

   # Customize the chart layout for clarity
   fig.update_layout(
       yaxis_title="LGA",
       xaxis_title="Total TB Cases Notified",
       showlegend=False,  # Remove unnecessary legend
   )
   

   return fig

def plot_yearly_tb_cases():

    yearly_tb_cases = block2a.groupby('Year', as_index=False)['Total TB Cases notified'].sum()

    # Generate the line chart with Plotly Express
    fig = px.line(
        yearly_tb_cases,
        x="Year",
        y="Total TB Cases notified",
        markers=True,
        line_shape="linear",
        title=f"How many TB cases occur per year?<br><sup>Data from 2019 to 2023 of block2a</sup>",
    )

    # Customize the chart layout for clarity
    fig.update_layout(
        xaxis_title="Year and Quarter",
        yaxis_title="Total TB Cases notified",
    )

    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = [2019, 2020, 2021, 2022, 2023],
            ticktext = [2019, 2020, 2021, 2022, 2023]
        )
    )

    return fig
