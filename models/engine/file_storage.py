import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    A class to manage persistent storage of objects in a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary of objects stored in the file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return a dictionary of all objects in storage.

        Returns:
            dict: A dictionary of all objects, with keys in the format "<class name>.<object id>".
        """
        return self.__objects

    def new(self, obj):
        """
        Add an object to storage.

        Args:
            obj (BaseModel): The object to add to storage.
        """
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_key] = obj

    def save(self):
        """
        Save the current state of storage to the JSON file.
        """
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as fp:
            json.dump(obj_dict, fp)

    def reload(self):
        """
        Load objects from the JSON file into storage.
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as fp:
                json_obj = json.load(fp)
                for key, val in json_obj.items():
                    obj_class, *_ = key.split('.')
                    obj = globals()[obj_class](**val)
                    self.__objects[key] = obj
