'''
Yini Li
CS 5001, Fall 2023
Final Project

This is the main entry for the museum app
'''
import streamlit as st
from requests.exceptions import HTTPError, ConnectionError, Timeout, TooManyRedirects

from views.home import display_home_page
from views.quiz import display_quiz_page
from views.random_display import random_display_page
from views.data import display_data_page


def main():
    """
    Main function for a Streamlit application, handling page navigation and errors

    Args:
        Nothing

    Errors:
        ValueError: Handles errors related to inappropriate values passed to functions.
        TypeError: Catches errors where an object is of an unexpected type.
        Exception: If any issues occur during the request process (HTTP error, connection error, timeout, 
                   or redirect issues), a relevant error message is print as an exception.

    Returns:
        Nothing
    """
    try:
        with st.sidebar:
            navigation_options = ["Home", "Data", "Random display", "Quiz"]
            selected_navigation = st.selectbox("select page", navigation_options)
        if selected_navigation == "Home":
            display_home_page()
        if selected_navigation == "Data":
            display_data_page()
        if selected_navigation == "Quiz":
            display_quiz_page()
        if selected_navigation == "Random display":
            random_display_page()
    except ValueError as ex:
        print(type(ex), ex)
    except TypeError as ex:
        print(type(ex), ex)
    except HTTPError as ex:
        print(type(ex), ex)
    except ConnectionError as ex:
        print(type(ex), ex)
    except Timeout as ex:
        print(type(ex), ex)
    except TooManyRedirects as ex:
        print(type(ex), ex)


if __name__ == "__main__":
    main()
