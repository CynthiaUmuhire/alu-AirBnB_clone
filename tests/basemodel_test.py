#!/usr/bin/python3
""" test the base model class """

from models.base_model import BaseModel


model = BaseModel()
model.name = "My First Model"
model.my_number = 89
print(model)
model.save()
print(model)
my_model_json = model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                   my_model_json[key]))