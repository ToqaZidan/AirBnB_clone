#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Unit tests for the Review class."""

    def setUp(self):
        """Set up a new Review object for each test."""
        self.review = Review()

    def test_inherits_from_BaseModel(self):
        """Test that Review inherits from BaseModel."""
        self.assertIsInstance(self.review, BaseModel)

    def test_place_id_attribute(self):
        """Test the place_id attribute of Review class."""
        self.assertEqual(self.review.place_id, "")

    def test_user_id_attribute(self):
        """Test the user_id attribute of Review class."""
        self.assertEqual(self.review.user_id, "")

    def test_text_attribute(self):
        """Test the text attribute of Review class."""
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
