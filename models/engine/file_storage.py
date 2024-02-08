#!/usr/bin/python3
"""
Module:file_storage.py
"""

import os
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """
    create file storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return __objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as file:
            serialized_objects = {}
            for k, v in self.__objects.items():
                if hasattr(v, 'to_dict') and callable(getattr(v, 'to_dict')):
                    serialized_objects[k] = v.to_dict()
                else:
                    serialized_objects[k] = v
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        current_classes = {'BaseModel': BaseModel, 'User': User}

        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r') as file:
            deserialized = None

            try:
                deserialized = json.load(file)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            self.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}
