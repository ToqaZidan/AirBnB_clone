#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class."""

    def setUp(self):
        """Set up a new Amenity object for each test."""
        self.amenity = Amenity()

    def test_inherits_from_BaseModel(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_name_attribute(self):
        """Test the name attribute of Amenity class."""
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
