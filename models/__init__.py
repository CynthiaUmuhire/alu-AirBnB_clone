#!/usr/bin/python3
"""
The method(__init__) for models directory
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
classes = {"BaseModel": BaseModel}
