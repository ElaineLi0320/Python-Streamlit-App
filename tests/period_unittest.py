'''
Yini Li
CS 5001, Fall 2023
Final Project

This is the unittest file for the final project
'''

import unittest
from models.period import Period
from models.period import ANCIENT_CLASSICAL, MEDIEVAL, RENAISSANCE, ROMANTICISM, MODERN, CONTEMPORARY


class TestPeriod(unittest.TestCase):
    def setUp(self):
        """
        Setup a test Period instance for testing.
        """
        self.period = Period()
        self.mock_ids = [1, 2, 3, 4, 5]
        self.mock_years = [ANCIENT_CLASSICAL, MEDIEVAL, RENAISSANCE, ROMANTICISM, MODERN, CONTEMPORARY]

    def test_add_sample_artworks_ids(self):
        """
        Test add IDs to the Period instance.
        """
        for id in self.mock_ids:
            self.period.add_sample_artworks_ids(id)
        self.assertEqual(self.period.ids, self.mock_ids)

    def test_add_sample_artworks_ids_with_invalid_type(self):
        """
        Test adding an invalid ID type raises TypeError.
        """
        with self.assertRaises(TypeError):
            self.period.add_sample_artworks_ids("invalid_id")

    def test_add_sample_artworks_data(self):
        """
        Test add years to the Period instance.
        """
        for year in self.mock_years:
            self.period.add_sample_artworks_data(year)
        self.assertEqual(self.period.artwork_completed_year_list, self.mock_years)

    def test_add_sample_artworks_data_with_invalid_type(self):
        """
        Test adding an invalid year type raises TypeError.
        """
        with self.assertRaises(TypeError):
            self.period.add_sample_artworks_data("invalid_year")

    def test_count_periods(self):
        """
        Test count occurrences of each art period.
        """
        for year in self.mock_years:
            self.period.add_sample_artworks_data(year)
        self.period.count_sample_art_periods()

        expected_counts = {
            "Ancient_Classical": 1,
            "Medieval": 1,
            "Renaissance": 1,
            "Romanticism": 1,
            "Modern": 1,
            "Contemporary": 1
        }
        self.assertEqual(self.period.art_period_counts, expected_counts)

    def test_empty_data(self):
        """
        Test edge case: empty data
        """
        counts = self.period.count_sample_art_periods()
        for count in counts.values():
            self.assertEqual(count, 0)

# Command
# python3 -m unittest tests.period_unittest
