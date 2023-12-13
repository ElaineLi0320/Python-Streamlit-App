'''
Yini Li
CS 5001, Fall 2023
Final Project

This is the random display page for the museum app
'''
import streamlit as st
import random
from models.gallery import Gallery
from utils.fetch_data import get_highlighted_artworks_ids, fetch_highlighted_artworks_images


def display_image(gallery):
    """
    Displays a random image from the gallery.

    Args:
        gallery (Gallery): An instance of the Gallery class with loaded images.

    Raises:
        TypeError: If 'gallery' is not an instance of the Gallery class.
        ValueError: If the 'gallery_images' attribute of the gallery is empty.
    """
    if not isinstance(gallery, Gallery):
        raise TypeError("gallery must be an instance of the Gallery class")

    if not gallery.gallery_images:
        raise ValueError("No images available in the gallery.")

    random_index = random.randint(0, len(gallery.gallery_images) - 1)
    image_url = gallery.get_gallery_item(random_index)
    st.image(image_url, caption=f"Artwork ID: {gallery.ids[random_index]}")


def random_display_page():
    """
    Displays a page in a Streamlit application that showcases highlighted artworks.

    Args:
        Nothing

    Returns:
        Nothing
    """
    gallery = Gallery()
    get_highlighted_artworks_ids(gallery)
    for object_id in gallery.ids:
        fetch_highlighted_artworks_images(object_id, gallery)
    # Display the title and header
    st.title("Highlighted Artworks display!")
    # display images
    if st.button('Click to display'):
        display_image(gallery)
