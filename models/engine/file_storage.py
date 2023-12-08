#!/usr/bin/python3
"""This module contains the class FileStorage"""

import json
import os
from datetime import datetime


class FileStorage():
    """
    Defines the class FileStorage

    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dictionary): Where all the JSON objects will be stored

    Methods:
        all(Self): Returns the dictionary __objects
        new(self, obj): Stores new object inside __objects
        save(self): serializes __objects to JSON file
        reload(self): deserializes the JSON file to __objects
    """
    __file_path = "bigdata.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Stores new object inside __objects"""

        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON file"""

        objs_dict = {}
        for key, value in FileStorage.__objects.items():
            objs_dict[key] = value.to_dict()

        json_content = json.dumps(objs_dict, default=format_datetime)

        with open(FileStorage.__file_path, "w") as file:
            file.write(json_content)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                content = file.read()
                python_objects = json.loads(content)

                for key, value in python_objects.items():
                    FileStorage.__objects[key] = BaseModel(**value)


def format_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
