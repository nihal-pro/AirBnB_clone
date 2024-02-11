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
        models.storage.new(self)

    def __str__(self):
        """
        return the string of instences
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        update updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict methode
        """
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        if isinstance(self.created_at, datetime):
            dict['created_at'] = self.created_at.isoformat()
        else:
            dict['created_at'] = self.created_at
        if isinstance(self.updated_at, datetime):
            dict['updated_at'] = self.updated_at.isoformat()
        else:
            dict['updated_at'] = self.updated_at
        return dict
