#!/usr/bin/python3
"""
File Storage Module
This module is in charge of the storage of the classes
"""
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

    def __init__(self):
        """initialize file storage"""
        self.__file_path = "file.json"
        self.__objects = {}

        try:
            with open(self.__file_path, 'r') as file:
                data = file.read()
                if data:
                    self.__objects = json.loads(data)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Error: Invalid JSON data in file.json")

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
        try:
            obj_dict = {}
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()

            with open(self.__file_path, 'w') as file:
                json.dump(obj_dict, file)
        except Exception as e:
            print(f"Error: Failed to save data to file.json: {e}")

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists).
        """
        try:
            with open(self.__file_path, 'r') as file:
                if file.read().strip() != "":
                    file.seek(0)  # Reset the file pointer to the beginning
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        cls_name = key.split(".")[0]
                        obj = models.classes[cls_name](**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass  # Ignore the error if the file doesn't exist
        except Exception as e:
            print(f"Error: Failed to reload data from file.json: {e}")
