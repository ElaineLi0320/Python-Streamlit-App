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

# Constants
MALE_ARTISTS_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search?q=male"
FEMALE_ARTISTS_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/search?q=female"


class TestFetchGenderData(unittest.TestCase):
    # test functions for fetching artists' gender data
    def test_fetch_male_artists_data(self):
        test_url = MALE_ARTISTS_API_URL

        excepted_data = {
            "total": 10,
            "objectIDs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }

        with requests_mock.Mocker() as m:
            m.get(test_url, json=excepted_data)
            response = requests.get(test_url)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['total'], 10)

    def test_fetch_male_artists_data_with_http_error(self):
        test_url = MALE_ARTISTS_API_URL

        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_fetch_male_artists_data_with_connection_error(self):
        test_url = MALE_ARTISTS_API_URL

        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_fetch_female_artists_data(self):
        test_url = FEMALE_ARTISTS_API_URL

        excepted_data = {
            "total": 10,
            "objectIDs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }

        with requests_mock.Mocker() as m:
            m.get(test_url, json=excepted_data)
            response = requests.get(test_url)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['total'], 10)

    def test_fetch_female_artists_data_with_http_error(self):
        test_url = FEMALE_ARTISTS_API_URL

        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_fetch_female_artists_data_with_connection_error(self):
        test_url = FEMALE_ARTISTS_API_URL

        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

# Command
# python3 -m unittest tests.fetch_gender_data_unittest
