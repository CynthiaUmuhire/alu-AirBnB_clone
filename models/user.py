#!/usr/bin/python3
"""This Is A Module That Creates A Uaer Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Object Management Class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
