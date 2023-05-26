#!/usr/bin/python3
"""
User Class Base model That create user class from base model.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
