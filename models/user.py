#!usr/bin/python3
"""
Module:usr.py
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    create new user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
