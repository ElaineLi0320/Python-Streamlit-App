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
import random
from models.period import Period
from utils.fetch_data import fetch_sample_artworks_period_data

# Constants
ARTWORKS_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
GET_OBJECT_API_URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects"


class TestFetchPeriodData(unittest.TestCase):
    # test functions for fetching sample ids for artworks' period
    def test_get_period_ids(self):
        period = Period()
        sample_size = 5
        test_url = ARTWORKS_API_URL

        expected_data = {
            "total": 10,
            "objectIDs": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }

        with requests_mock.Mocker() as m:
            m.get(test_url, json=expected_data)
            response = requests.get(test_url)
            ids = response.json().get('objectIDs', [])
            sample_ids = random.sample(ids, sample_size)

            for object_id in sample_ids:
                period.add_sample_artworks_ids(object_id)

            for id in sample_ids:
                self.assertIn(id, expected_data["objectIDs"])

    def test_get_period_ids_with_http_error(self):
        test_url = ARTWORKS_API_URL

        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_get_period_ids_with_connection_error(self):
        test_url = ARTWORKS_API_URL

        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    # test functions for fetching periods' sample data
    def test_fetch_periods_data_success(self):
        with requests_mock.Mocker() as m:
            object_id = 123
            expected_url = f"{GET_OBJECT_API_URL}/{object_id}"
            mock_response = {"objectEndDate": 2022}
            m.get(expected_url, json=mock_response)
            period = Period()
            result = fetch_sample_artworks_period_data(object_id, period)
            self.assertEqual(result, period)

    def test_fetch_periods_data_with_http_error(self):
        gallery = Period()
        object_id = 1
        gallery.add_sample_artworks_ids(object_id)
        test_url = f"{GET_OBJECT_API_URL}/{object_id}"
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(ConnectionError)

    def test_fetch_periods_data_with_connection_error(self):
        gallery = Period()
        object_id = 1
        gallery.add_sample_artworks_ids(object_id)
        test_url = f"{GET_OBJECT_API_URL}/{object_id}"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

# Command
# python3 -m unittest tests.fetch_period_data_unittest
