#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage


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


if __name__ == "__main__":
    unittest.main()
