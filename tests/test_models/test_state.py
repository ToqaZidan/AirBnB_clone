#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Unit tests for the State class."""

    def setUp(self):
        """Set up a new State object for each test."""
        self.state = State()

    def test_inherits_from_BaseModel(self):
        """Test that State inherits from BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_name_attribute(self):
        """Test the name attribute of State class."""
        self.assertEqual(self.state.name, "")


if __name__ == "__main__":
    unittest.main()
