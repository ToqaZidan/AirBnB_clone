#!/usr/bin/python3


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    @property
    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects = 
