'''
Yini Li
CS 5001, Fall 2023
Final Project

This is the data page for the museum app
'''
import streamlit as st

from models.period import Period
from utils.fetch_data import fetch_male_artists_data, fetch_female_artists_data
from utils.fetch_data import get_sample_artworks_ids, fetch_sample_artworks_period_data
import pandas as pd
import matplotlib.pyplot as plt


# Pie chart: artists' gender
def create_pie_chart(male, female):
    """
    Creates a pie chart representing the distribution of male and female artists.
    It checks the validity of input values to ensure they are positive integers before creating the chart.

    Args:
        male (int): The number of male artists. Must be a positive integer.
        female (int): The number of female artists. Must be a positive integer.

    Returns:
        matplotlib.figure.Figure: A matplotlib figure object containing the pie chart.

    Raises:
        ValueError: If either 'male' or 'female' is not an integer or if their values are 
                    not positive integers.
    """
    if not isinstance(male, int) or not isinstance(female, int):
        raise ValueError("Both male and female values must be integers")

    if male <= 0 or female <= 0:
        raise ValueError("Values for male and female artists should be positive")

    labels = 'Male Artists', 'Female Artists'
    sizes = [male, female]

    figure, axis = plt.subplots()
    axis.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    axis.axis('equal')

    return figure


# Bar chart: art period
def convert_data_to_dataframe(period_counts):
    """
    Converts a dictionary to a pandas DataFrame.

    Args:
        period_counts (dict): A dictionary with art period names as keys and their counts as values.

    Returns:
        pd.DataFrame: A pandas DataFrame created from the dictionary.
    """
    data_frame = pd.DataFrame(list(period_counts.items()), columns=['Art Period', 'Count'])
    return data_frame


def create_chart_with_pandas(period_counts):
    """
    Creates a bar chart using pandas and Streamlit's built-in function.

    Args:
        period_counts (dict): A dictionary with art period names as keys and their counts as values.

    Returns:
        pd.DataFrame: A pandas DataFrame for plotting with st.bar_chart.

    Raises:
        TypeError: If 'period_counts' is not a dictionary.
        ValueError: If any count in 'period_counts' is not a non-negative number.
    """
    if not isinstance(period_counts, dict):
        raise TypeError("period_counts must be a dictionary.")

    for key, value in period_counts.items():
        if not isinstance(value, int):
            raise ValueError(f"The count for '{key}' must be an integer")

        if value < 0:
            raise ValueError(f"The count for '{key}' must be non-negative")

    df = convert_data_to_dataframe(period_counts)
    return df.set_index('Art Period')


def display_data_page():
    """
    Displays a data page in a Streamlit application.

    Args:
        Nothing

    Returns:
        Nothing
    """
    st.title("Have a glance?")

    # Gender Distribution of Artists
    if st.button('Show Gender Distribution of Artists'):
        st.header("Gender Distribution of Artists")
        male_artists = fetch_male_artists_data()
        female_artists = fetch_female_artists_data()
        pie_chart = create_pie_chart(male_artists, female_artists)
        st.pyplot(pie_chart)
    # Art Period Distribution of Artworks
    if st.button('Show Art Period Distribution of Artworks'):
        st.header("Art Period Distribution of Artworks")
        st.write("This is a bar chart detailing the distribution of artworks across different art periods from a sample of size 100.")
        st.write("Categories include Ancient_Classical, Medieval, Renaissance, Romanticism, Modern and Contemporary.")
        st.write("Each category's corresponding bar height represents the number of artworks attributed to that period.")
        period = Period()
        get_sample_artworks_ids(period)
        for object_id in period.ids:
            fetch_sample_artworks_period_data(object_id, period)
        period_dict = period.count_sample_art_periods()
        st.write(period_dict)
        chart_data = create_chart_with_pandas(period_dict)
        st.bar_chart(chart_data)
