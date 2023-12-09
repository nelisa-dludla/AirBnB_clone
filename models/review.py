#!/usr/bin/python3
"""This module contains the class Review"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    Defines the Review class

    Attributes:
        place_id (str): Id of Place
        user_id (str): Id of User
        text (str): Review text
    """

    place_id = ""
    user_id = ""
    text = ""
