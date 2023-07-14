#!/usr/bin/python3
import json
import os


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    @property
    def all(self):
        return self.__objects

    def new(self, obj):
        setattr(self.__objects, f"{obj.__class__.__name__}.{obj.id}", obj)

    def save(self):
        with open(self.__file_path, 'w') as fp:
            json.dump(self.__objects, fp)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as fp:
                self.__objects = json.load(fp)
