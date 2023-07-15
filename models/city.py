#!/usr/bin/python3
"""
City Module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class

    Attributes:
    - state_id: string - empty string: it will be the State.id
    - name: string - empty string
    """
    state_id = ''
    name = ''
