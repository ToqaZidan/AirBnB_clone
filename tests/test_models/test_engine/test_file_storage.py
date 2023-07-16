#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import json
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from os import path


class TestFileStorage(unittest.TestCase):
    """
    A class to test the FileStorage class.
    """

    def setUp(self):
        """
        Initialize a new FileStorage object for each test.
        """
        self.storage = storage

    def test_new_adds_object_to_storage(self):
        """
        Test that new() method adds an object to storage.
        """
        obj = BaseModel()
        self.storage.new(obj)
        result = self.storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", result)

    def test_save_writes_to_file(self):
        """
        Test that save() method writes objects to the file.
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, 'r') as fp:
            result = fp.read()
            self.assertIn(f"{obj.__class__.__name__}.{obj.id}", result)

    def test_reload_reads_from_file(self):
        """
        Test that reload() method reads objects from the file.
        """
        obj = BaseModel()
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()

        result = self.storage.all()
        self.assertIn(obj_key, result)

    def test_new(self):
        """ New object is correctly added to __objects """
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_all_returns_dict(self):
        """ all() returns a dictionary """
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_all_returns_correct_dict(self):
        """ all() returns the correct dictionary """
        obj1 = BaseModel()
        obj2 = Amenity()
        self.storage.new(obj1)
        self.storage.new(obj2)
        result = self.storage.all()
        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", result)
        self.assertIn(f"{obj2.__class__.__name__}.{obj2.id}", result)

    def test_save_file_exists(self):
        """ save() creates the file """
        self.storage.save()
        self.assertTrue(path.exists(self.storage._FileStorage__file_path))

    def test_reload_file_not_found(self):
        """ reload() doesn't raise an exception if file not found """
        self.storage.reload()
        # No assertion needed, test passes if no exception is raised

    def test_reload_file_exists(self):
        """ reload() loads objects from existing file """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        result = self.storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", result)

    def test_reload_deserialization(self):
        """ reload() correctly deserializes objects """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        result = self.storage.all()
        self.assertEqual(obj_dict, result[f"{obj.__class__.__name__}.{obj.id}"].to_dict())


if __name__ == "__main__":
    unittest.main()
