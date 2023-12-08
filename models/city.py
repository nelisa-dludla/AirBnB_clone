#!/usr/bin/python3
"""This module contains the class City"""

from .base_model import BaseModel


class City(BaseModel):
    """
    Defines the City class

    Attributes:
        state_id (str): Id of State
        name (str): Name of the state
    """

    state_id = ""
    name = ""
