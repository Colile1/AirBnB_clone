#!/usr/bin/python3
"""
This module defines a review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel

    Attributes:
        place_id (str): The place ID
        user_id (str): The user ID
        text (str): The review text
    """
    place_id = ""
    user_id = ""
    text = ""
