#!/usr/bin/python3
"""This module contains the class FileStorage"""

import json
import os


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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to JSON file"""

        json_content = json.dumps(FileStorage.__objects)

        with open(FileStorage.__file_path, "w") as file:
            file.write(json_content)

    def reload(self):
        """deserializes the JSON file to __objects"""

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                content = file.read()
                python_objects = json.loads(content)
                FileStorage.__objects.update(python_objects)
