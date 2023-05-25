#!/usr/bin/python3
"""
This is the base class for all models in the project.
"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """
    Defining Methods and attributes of the Basemodel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Base model constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        models.storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with a new value.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a copy of the instance dictionary
        """
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj

    def __str__(self):
        """
        String representation of the instance class
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
