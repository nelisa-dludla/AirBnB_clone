#!/usr/bin/python3
"""This module contains the class BaseModel"""

from uuid import uuid4
from datetime import datetime
from . import storage


class BaseModel():
    """
    Defines the class BaseModel

    Attributes:
        id (int): Id for the current instance
        created_at (str): The date and time the instance was created
        updated_at (str): The date and time the instance was updated

    Methods:
        __init__(self, *args, **kwargs): Initializes a new BaseModel instance
        save(self): Updates the current instance with the current datetime
        to_dict(self): Returns a dictionary represention of __dict__
        __str__(self): Returns a string representation of the instance
    """

    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    format = "%Y-%m-%dT%H:%M:%S.%f"
                    new_value = datetime.strptime(value, format)

                    setattr(self, key, new_value)

                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = BaseModel.id
            self.created_at = BaseModel.created_at
            self.updated_at = BaseModel.updated_at
            storage.new(self)

    def save(self):
        """Updates the current instance with the current datetime"""

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary represention of __dict__ of the instance"""

        result_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                result_dict[f"{key}"] = f"{value.isoformat()}"
            else:
                result_dict[f"{key}"] = f"{value}"

        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """Returns a string representation of the instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
