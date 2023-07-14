#!/usr/bin/python3
'''
Base class module defines all common attributes/methods for other classes
'''
import uuid
from datetime import datetime
import models


class BaseModel():
    """Base class for other classes.

    Attributes:
        id (str): The unique identifier of the object.
        created_at (datetime): The date and time the object was created.
        updated_at (datetime): The date and time the object was last updated.
    """

    def __init__(self, *args, **kwargs):
        """Instantiate a BaseModel object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None.
        """
        if kwargs:
            if kwargs["__class__"] == self.__class__.__name__:
                self.id, self.created_at, self.updated_at, *_ = kwargs.values()
                self.created_at = datetime.strptime(
                        self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
                self.updated_at = datetime.strptime(
                        self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel object.

        Returns:
            str: A string representation of the BaseModel object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the value of updated_at to the current datetime.

        Returns:
            None.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel object.

        Returns:
            dict: A dictionary representation of the BaseModel object.
        """
        obj_dict = {**(self.__dict__), "__class__": self.__class__.__name__}
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
