#!/usr/bin/python3
import uuid
from datetime import datetime
'''
Base class module defines all common attributes/methods for other classes
'''


class BaseModel():
    '''
    Base class common attributes/methods for other classes
    '''
    def __init__(self, *args, **kwargs):
        """
        Instantiate BaseModel object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

    def __str__(self):
        """
        return a string representation of the BaseModel object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the value of updated_at to the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        my_dict = {**(self.__dict__), "__class__": self.__class__.__name__}
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
