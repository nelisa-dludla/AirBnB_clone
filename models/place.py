#!/usr/bin/python3
"""This module contains the Place class"""

from .base_model import BaseModel


class Place(BaseModel):
    """
    Defines the Place class

    Attributes:
        city_id (str): Id of City
        user_id (str): Id of User
        name (str): Name of the place
        description (str): Description for the place
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum number of guests
        price_by_night (int): Price per night
        latitude (float): Latitudinal position
        longitude (float): Longitudinal position
        amenity_ids (list): List of Amenity ids
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
