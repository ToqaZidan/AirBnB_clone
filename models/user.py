#!/usr/bin/python3
"""
A user module that inherit from BaseModel class
and contain all user information.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Iniyialze User class

    Attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """

    email = ''
    password = ''
    first_name =''
    last_name = ''
