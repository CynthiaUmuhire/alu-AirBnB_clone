#!/usr/bin/python3
"""Tests """

from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    objects = all_objs[obj_id]
    print(objects)

print("-- Create a new object --")
model = BaseModel()
model.name = "My_First_Model"
model.my_number = 15
model.save()
print(model)
