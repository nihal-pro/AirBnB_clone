#!/usr/bin/python3
"""
Module:review.py
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    review class
    """
    text = ""
    user_id = ""
    place_id = ""
