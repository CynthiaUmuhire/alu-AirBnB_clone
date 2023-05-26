#!/usr/bin/python3
"""
This Is The Review class from the base model.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A Review Class Docs"""
    place_id = ""
    user_id = ""
    text = ""
