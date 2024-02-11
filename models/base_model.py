#!/usr/bin/python3
"""
Module:base_model.py
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    create class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes BaseModel instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        return the string of instences
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        update updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """to_dict methode
        """
        dict = self.__dict__
        dict['__class__'] = type(self).__name__
        if isinstance(self.created_at, datetime):
            dict['created_at'] = self.created_at.isoformat()
        else:
            dict['created_at'] = self.created_at
        if isinstance(self.updated_at, datetime):
            dict['updated_at'] = self.updated_at.isoformat()
        else:
            dict['updated_at'] = self.updated_at
        return dict
