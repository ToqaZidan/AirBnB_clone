#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import path


class FileStorage:
    """
    This class that serialize and deserialize instances of models
    to and from a JSON file.
    It maintains a dictionary of objects, where the keys are
    in the format "<class name>.<object id>". The dictionary is saved
    to a JSON file for persistence.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store the instances
            by their class name and id.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all objects stored in the __objects dictionary.

        Returns:
            dict: A dictionary containing all the objects stored.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj: The object instance to be added.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects stored in the __objects dictionary
        and saves them to a JSON file.
        """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the objects from the JSON file and stores
        them in the __objects dictionary.
        If the JSON file does not exist, no exception is raised.
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
