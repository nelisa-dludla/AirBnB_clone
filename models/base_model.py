#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel():
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = created_at

    def __init__(self):
        self.id = BaseModel.id
        self.created_at = BaseModel.created_at.now()
        self.updated_at = BaseModel.updated_at

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        result_dict = {}
        for key, value in self.__dict__.items():
            result_dict[f"{key}"] = f"{value}"

        return result_dict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

