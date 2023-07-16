#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Unit tests for the City class."""

    def setUp(self):
        """Set up a new City object for each test."""
        self.city = City()

    def test_inherits_from_BaseModel(self):
        """Test that City inherits from BaseModel."""
        self.assertIsInstance(self.city, BaseModel)

    def test_state_id_attribute(self):
        """Test the state_id attribute of City class."""
        self.assertEqual(self.city.state_id, "")

    def test_name_attribute(self):
        """Test the name attribute of City class."""
        self.assertEqual(self.city.name, "")


if __name__ == "__main__":
    unittest.main()
