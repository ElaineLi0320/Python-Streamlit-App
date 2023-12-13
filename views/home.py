'''
Yini Li
CS 5001, Fall 2023
Final Project

This is the home page for the museum app
'''
import streamlit as st


def display_home_page():
    """
    Displays the home page of a Streamlit application for a virtual museum experience.

    Args:
        Nothing

    Returns:
        Nothing
    """
    st.title("Museum App")
    st.write("Welcome to The Metropolitan Museum of Art!")
    st.write("Looking for a museum experience without leaving home? This website provides an easy-approached way for you to explore the exhibits of the Metropolitan Museum of Art.")
    st.write("Explore now!")