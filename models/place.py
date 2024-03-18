#!/usr/bin/python3
"""
This module defines a Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel

    Attributes:
        city_id (str): The city ID
        user_id (str): The user ID
        name (str): The name of the place
        description (str): Description of the place
        number_rooms (int): The number of rooms
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The maximum number of guests allowed
        price_by_night (int): The price per night
        latitude (float): Latitude coordinate of the place
        longitude (float): Longitude coordinate of the place
        amenity_ids (list): List of amenity IDs
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
