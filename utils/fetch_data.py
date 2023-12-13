'''
Yini Li
CS 5001, Fall 2023
Final Project

This is the functions file for the final project
This file holds all the functions for fetching and cleaning data from the API
'''
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, TooManyRedirects
import random

# Constants
ARTWORKS_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
MALE_ARTISTS_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search?q=male"
FEMALE_ARTISTS_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search?q=female"
HIGHLIGHTED_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&q=isHighlight"
GET_OBJECT_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"


# Get artists' gender data
def fetch_male_artists_data():
    """
    Fetch male artists' data

    Args:
        Nothing

    Returns:
        total (int): The total number of male artist

    Exception: If any issues occur during the request process (HTTP error, connection error, timeout, 
               or redirect issues), a relevant error message is print as an exception.
    """
    try:
        response = requests.get(MALE_ARTISTS_API_URL)
        response.raise_for_status()
        data = response.json()
        total = data["total"]
        return total
    except HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
    except ConnectionError as connection_error:
        print(f"Connection error occurred: {connection_error}")
    except Timeout as timeout_error:
        print(f"Timeout error occurred: {timeout_error}")
    except TooManyRedirects as redirect_error:
        print(f"Redirect error occurred: {redirect_error}")


def fetch_female_artists_data():
    """
    Fetch female artists' data

    Args:
        Nothing

    Returns:
        total (int): The total number of male artists

    Exception: If any issues occur during the request process (HTTP error, connection error, timeout, 
               or redirect issues), a relevant error message is print as an exception.
    """
    try:
        response = requests.get(FEMALE_ARTISTS_API_URL)
        response.raise_for_status()
        data = response.json()
        total = data["total"]
        return total
    except HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
    except ConnectionError as connection_error:
        print(f"Connection error occurred: {connection_error}")
    except Timeout as timeout_error:
        print(f"Timeout error occurred: {timeout_error}")
    except TooManyRedirects as redirect_error:
        print(f"Redirect error occurred: {redirect_error}")


# Get highlighted artworks' gallery
def get_highlighted_artworks_ids(gallery):
    """
    Get ids for highlighted artworks

    Args:
        gallery (GalleryType): An object representing a gallery, which have an 'add_id' method to add the fetched artwork IDs.

    Returns:
        gallery (GalleryType): The same gallery object provided as an argument, now updated with the IDs of the highlighted artworks.

    Exception: If any issues occur during the request process (HTTP error, connection error, timeout, 
               or redirect issues), a relevant error message is print as an exception.
    """
    try:
        response = requests.get(HIGHLIGHTED_API_URL)
        response.raise_for_status()
        data = response.json()
        ids = data['objectIDs']
        for object_id in ids:
            gallery.add_gallery_artwork_id(object_id)
        return gallery
    except HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
    except ConnectionError as connection_error:
        print(f"Connection error occurred: {connection_error}")
    except Timeout as timeout_error:
        print(f"Timeout error occurred: {timeout_error}")
    except TooManyRedirects as redirect_error:
        print(f"Redirect error occurred: {redirect_error}")
    except ValueError as value_error:
        print(f"ValueError occurred: {value_error}")


def fetch_highlighted_artworks_images(object_id, gallery):
    """
    Fetch highlighted objects data

    Args:
        object_id (int/str): The ID of the object to fetch data for.
        gallery (GalleryType): An object representing a gallery, which have a 'gallery_images' attribute 
                               where images can be appended.

    Returns:
        gallery (GalleryType): The same gallery object provided as an argument, updated with the primary image 
                               of the highlighted object if applicable.

    Exception: If any issues occur during the request process (HTTP error, connection error, timeout, 
               or redirect issues), a relevant error message is print as an exception.
    """
    url = f"{GET_OBJECT_API_URL}/{object_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["isHighlight"] is True and data["primaryImage"] != "":
            gallery.gallery_images.append(data["primaryImage"])
            return gallery
    except HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
    except ConnectionError as connection_error:
        print(f"Connection error occurred: {connection_error}")
    except Timeout as timeout_error:
        print(f"Timeout error occurred: {timeout_error}")
    except TooManyRedirects as redirect_error:
        print(f"Redirect error occurred: {redirect_error}")
    except ValueError as value_error:
        print(f"ValueError occurred: {value_error}")


# Get artworks' period data
def get_sample_artworks_ids(period, sample_size=100):
    """
    Get a sample ids of size 100

    Args:
        period (PeriodType): An object representing a period, which have an 'add_id' method 
                             to add the fetched artwork IDs.
        sample_size (int, optional): The number of IDs to sample. Defaults to 300.

    Returns:
        period (PeriodType): The same period object provided as an argument, updated with the sampled IDs.

    Raises:
        ValueError: If the sample size is larger than the total number of IDs available.
        Prints error messages for HTTP error, connection error, timeout, redirect issues, or JSON value errors.
    """
    try:
        response = requests.get(ARTWORKS_API_URL)
        response.raise_for_status()
        data = response.json()
        ids = data['objectIDs']
        if len(ids) >= sample_size:
            sample_ids = random.sample(ids, sample_size)
            for object_id in sample_ids:
                period.add_sample_artworks_ids(object_id)
        else:
            raise ValueError("Sample size is bigger than the total number of Ids")
        return period
    except HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
    except ConnectionError as connection_error:
        print(f"Connection error occurred: {connection_error}")
    except Timeout as timeout_error:
        print(f"Timeout error occurred: {timeout_error}")
    except TooManyRedirects as redirect_error:
        print(f"Redirect error occurred: {redirect_error}")
    except ValueError as value_error:
        print(f"ValueError occurred: {value_error}")


def fetch_sample_artworks_period_data(object_id, period):
    """
    Fetch sample data

    Args:
        object_id (int/str): The ID of the object to fetch data for.
        period (PeriodType): An object representing a period, which have an 'add_data' method 
                             to add the fetched period data.

    Returns:
        period (PeriodType): The same period object provided as an argument, updated with the end date 
                             data of the object if applicable.

    Exception: If any issues occur during the request process (HTTP error, connection error, timeout, 
               or redirect issues), a relevant error message is print as an exception.
    """
    url = f"{GET_OBJECT_API_URL}/{object_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["objectEndDate"] != "":
            period.add_sample_artworks_data(data["objectEndDate"])
        return period
    except HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")
    except ConnectionError as connection_error:
        print(f"Connection error occurred: {connection_error}")
    except Timeout as timeout_error:
        print(f"Timeout error occurred: {timeout_error}")
    except TooManyRedirects as redirect_error:
        print(f"Redirect error occurred: {redirect_error}")
    except ValueError as value_error:
        print(f"ValueError occurred: {value_error}")
