'''
Yini Li
CS 5001, Fall 2023
Final Project

This is the unittest file for the final project
'''

import requests
from requests.exceptions import HTTPError, ConnectionError
import unittest
import requests_mock
from models.gallery import Gallery
from utils.fetch_data import fetch_highlighted_images

# Constants
HIGHLIGHTED_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&q=isHighlight"
GET_OBJECT_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"


class TestFetchGalleryData(unittest.TestCase):
    # test functions for fetching highlighted artworks' ids
    def test_get_highlighted_ids(self):
        gallery = Gallery()
        test_url = HIGHLIGHTED_API_URL

        expected_data = {
            "total": 10,
            "objectIDs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }

        with requests_mock.Mocker() as m:
            m.get(test_url, json=expected_data)
            response = requests.get(test_url)
            ids = response.json().get('objectIDs', [])

            for object_id in ids:
                gallery.add_id(object_id)

            for id in range(1, 11):
                self.assertIn(id, gallery.ids)

    def test_get_highlighted_ids_with_http_error(self):
        test_url = HIGHLIGHTED_API_URL

        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_get_highlighted_ids_with_connection_error(self):
        test_url = HIGHLIGHTED_API_URL

        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    # test functions for fetching highlighted artworks' images
    def test_fetch_highlighted_images_success(self):
        with requests_mock.Mocker() as m:
            gallery = Gallery()
            object_id = 1
            gallery.add_id(object_id)
            expected_url = f"{GET_OBJECT_API_URL}/{object_id}"
            mock_response = {"isHighlight": True, "primaryImage": "http://example.com/image.jpg"}
            m.get(expected_url, json=mock_response)
            result = fetch_highlighted_images(object_id, gallery)
            # Fetch the image at index 0
            image = result.get_item(0)
            self.assertEqual(image, "http://example.com/image.jpg")

    def test_fetch_highlighted_images_with_http_error(self):
        gallery = Gallery()
        object_id = 1
        gallery.add_id(object_id)
        test_url = f"{GET_OBJECT_API_URL}/{object_id}"
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(ConnectionError)

    def test_fetch_highlighted_images_with_connection_error(self):
        gallery = Gallery()
        object_id = 1
        gallery.add_id(object_id)
        test_url = f"{GET_OBJECT_API_URL}/{object_id}"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

# Command
# python3 -m unittest tests.fetch_gallery_data_unittest
