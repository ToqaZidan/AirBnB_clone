#!/usr/bin/python3
"""
A Super BaseModel class that defines all common
attributes/methods for other inherited classes of
the HBNB project; AIRBNB clone.
"""

import uuid
from datetime import datetime


class BaseModel():
    """
    Defining a super class BaseModel which other classes
    can inherit these common attributes and methods
    and have the functionality described.

    Attributes:
    id (str): string assigned to universal unique identifier.
    created_at (datetime): current datetime when instance created.
    updated_at (datetime): current datetime when an instance is created
        and it will be updated every time that object changes.

    """
    # re-create an instance with dictionary representation.
    def __init__(self, *args, **kwargs):
        """
        Initialize BaseModel class
        """
        if kwargs:
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """
        Updates the public instance attribute
        'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of
        the object's attributes.
        Copies the instance's __dict__ and
        adds the __class__ key with the class name.
        'created_at' and 'updated_at'converted to string object in ISO:
            format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Return the string representation of the class for the user.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )
