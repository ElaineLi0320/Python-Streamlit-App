'''
Yini Li
CS 5001, Fall 2023
Final Project

This is the unittest file for the final project
'''

import unittest
from models.gallery import Gallery


class TestGallery(unittest.TestCase):
    def setUp(self):
        """
        Set up a mock gallery for testing
        """
        self.gallery = Gallery()
        self.mock_ids = [100, 101, 102]
        self.mock_images = ["image1", "image2", "image3"]
        for id in self.mock_ids:
            self.gallery.add_gallery_artwork_id(id)
        self.gallery.gallery_images = self.mock_images

    def test_add_gallery_artwork_id_success(self):
        """
        Test adding IDs to the gallery.
        """
        new_id = 104
        self.gallery.add_gallery_artwork_id(new_id)
        self.assertIn(new_id, self.gallery.ids)

    def test_add_gallery_artwork_id_with_invalid_type(self):
        """
        Test adding a non-integer ID to the gallery.
        """
        with self.assertRaises(TypeError):
            self.gallery.add_gallery_artwork_id("not_an_int")

    def test_get_gallery_item_success(self):
        """
        Test getting an item by index.
        """
        index = 1
        expected_image = self.mock_images[index]
        retrieved_image = self.gallery.get_gallery_item(index)
        self.assertEqual(retrieved_image, expected_image)

    def test_get_gallery_item_with_non_integer_index(self):
        """
        Test getting an item with a non-integer index.
        """
        with self.assertRaises(TypeError):
            self.gallery.get_gallery_item("not_an_int")

    def test_get_gallery_item_with_invalid_index(self):
        """
        Test getting an item with an invalid index.
        """
        with self.assertRaises(IndexError):
            self.gallery.get_gallery_item(-1)
        with self.assertRaises(IndexError):
            self.gallery.get_gallery_item(len(self.mock_images))

    def test_gallery_with_no_items(self):
        """
        Test edge case: gallery is empty
        """
        self.gallery.ids = []
        self.gallery.gallery_images = []

        with self.assertRaises(IndexError):
            self.gallery.get_gallery_item(0)

# Command
# python3 -m unittest tests.gallery_unittest
