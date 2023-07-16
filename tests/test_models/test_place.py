#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Unit tests for the Place class."""

    def setUp(self):
        """Set up a new Place object for each test."""
        self.place = Place()

    def test_inherits_from_BaseModel(self):
        """Test that Place inherits from BaseModel."""
        self.assertIsInstance(self.place, BaseModel)

    def test_city_id_attribute(self):
        """Test the city_id attribute of Place class."""
        self.assertEqual(self.place.city_id, "")

    def test_user_id_attribute(self):
        """Test the user_id attribute of Place class."""
        self.assertEqual(self.place.user_id, "")

    def test_name_attribute(self):
        """Test the name attribute of Place class."""
        self.assertEqual(self.place.name, "")

    def test_description_attribute(self):
        """Test the description attribute of Place class."""
        self.assertEqual(self.place.description, "")

    def test_number_rooms_attribute(self):
        """Test the number_rooms attribute of Place class."""
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_attribute(self):
        """Test the number_bathrooms attribute of Place class."""
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_attribute(self):
        """Test the max_guest attribute of Place class."""
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_attribute(self):
        """Test the price_by_night attribute of Place class."""
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude_attribute(self):
        """Test the latitude attribute of Place class."""
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude_attribute(self):
        """Test the longitude attribute of Place class."""
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids_attribute(self):
        """Test the amenity_ids attribute of Place class."""
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
