#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel():
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = created_at

    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    format = "%Y-%m-%d %H:%M:%S.%f"
                    new_value = datetime.strptime(value, format)

                    setattr(self, key, new_value)

                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = BaseModel.id
            self.created_at = BaseModel.created_at.now()
            self.updated_at = BaseModel.updated_at

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        result_dict = {}
        for key, value in self.__dict__.items():
            result_dict[f"{key}"] = f"{value}"

        result_dict[f"__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

