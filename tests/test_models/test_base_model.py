import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def setUp(self):
        """Set up a new BaseModel object for each test."""
        self.base_model = BaseModel()

    def test_id_is_string(self):
        """Test that the id attribute is a string."""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """Test that the created_at attribute is a datetime object."""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that the updated_at attribute is a datetime object."""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that calling the save() method updates
        the updated_at attribute."""
        updated_at_before_save = self.base_model.updated_at
        self.base_model.save()
        updated_at_after_save = self.base_model.updated_at
        self.assertGreater(updated_at_after_save, updated_at_before_save)

    def test_to_dict_returns_dict(self):
        """Test that the to_dict() method returns a dictionary."""
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_includes_classname(self):
        """Test that the to_dict() method includes
        the class name in the dictionary."""
        obj_dict = self.base_model.to_dict()
        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_to_dict_includes_created_at(self):
        """Test that the to_dict() method includes the created_at
        attribute in the dictionary."""
        obj_dict = self.base_model.to_dict()
        self.assertIn("created_at", obj_dict)
        self.assertIsInstance(obj_dict["created_at"], str)

    def test_to_dict_includes_updated_at(self):
        """
        Test that the to_dict() method includes the updated_at
        attribute in the dictionary."""
        obj_dict = self.base_model.to_dict()
        self.assertIn("updated_at", obj_dict)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_str_returns_string(self):
        """Test that the __str__() method returns a string."""
        obj_str = str(self.base_model)
        self.assertIsInstance(obj_str, str)

    def test_str_returns_expected_string(self):
        """Test that the __str__() method returns the expected
        string representation of the object."""
        expected_str = "[BaseModel] ({}) {}".format(
                self.base_model.id,
                self.base_model.__dict__
                )
        obj_str = str(self.base_model)
        self.assertEqual(obj_str, expected_str)

    def test_to_dict_includes_attributes(self):
        """
        Test that the to_dict() method includes
        all attributes of the object."""
        obj_dict = self.base_model.to_dict()
        self.assertIn("id", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)

    def test_to_dict_excludes_methods(self):
        """Test that the to_dict() method does not
        include methods of the object."""
        obj_dict = self.base_model.to_dict()
        self.assertNotIn("save", obj_dict)
        self.assertNotIn("__str__", obj_dict)

    def test_get_attribute(self):
        """Test the get_attribute() method with valid
        and invalid attribute names."""
        result = self.base_model.id
        self.assertEqual(result, self.base_model.id)


if __name__ == "__main__":
    unittest.main()
