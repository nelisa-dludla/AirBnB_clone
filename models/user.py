#!/usr/bin/python3
"""This module contains the class"""

from .base_model import BaseModel


class User(BaseModel):
    """
    Defines the User class

    Attributes:
        email (str): Users email
        password (str): Users password
        first_name (str): Users first name
        last_name (str): Users last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
