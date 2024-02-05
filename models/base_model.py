#!/usr/bin/python3
"""
Module:base_model.py
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    create class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        initalisation of an object with it's
        attributes
        Args :
                Args(won't be used ): list of arguments
                Kwargs: pass in dictionary as arguments
        """
        if kwargs:
            for key, v in kwargs.items():
                if key != '__class__':
                    setattr(self, key, v)
                elif key in ('created_at', 'updated_at'):
                    Nv = datetime.fromisoformat(v)
                    setattr(self, key, Nv)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

    def to_dict(self):
        """
        return a dict containing all keys/values
        of ___dict__ of instance
        """
        dict = self.__dict__
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict
