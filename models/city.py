#!/usr/bin/python3
"""
This module defines a City class that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel

    Attributes:
        state_id (str): The state ID
        name (str): Name of the city
    """
    state_id = ""
    name = ""
