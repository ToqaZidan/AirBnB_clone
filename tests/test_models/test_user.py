#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unit tests for the User class."""

    def setUp(self):
        """Set up a new User object for each test."""
        self.user = User()

    def test_inherits_from_BaseModel(self):
        """Test that User inherits from BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_email_attribute(self):
        """Test the email attribute of User class."""
        self.assertEqual(self.user.email, "")

    def test_password_attribute(self):
        """Test the password attribute of User class."""
        self.assertEqual(self.user.password, "")

    def test_first_name_attribute(self):
        """Test the first_name attribute of User class."""
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attribute(self):
        """Test the last_name attribute of User class."""
        self.assertEqual(self.user.last_name, "")


if __name__ == "__main__":
    unittest.main()
