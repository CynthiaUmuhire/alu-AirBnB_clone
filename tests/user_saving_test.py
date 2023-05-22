#!/usr/bin/python3
"""Testing user saving"""

from models import storage
from models.user import User

all_objs = storage.all()
print("__Reloaded objects__")
for obj_id in all_objs.keys():
    object = all_objs[obj_id]
    print(object)

print("\n-- Create the first user --")
user1 = User()
user1.first_name = "Nate"
user1.last_name = "DUNKAN"
user1.email = "Ndunkan@gmail.com"
user1.password = "L.o.v.e"

print("\n-- Create the second user --")
user2 = User()
user2.first_name = "Kristina"
user2.last_name = "Michaelson"
user2.email = "kristina@gmail.com"
user2.password = "come"

print("\n-- Create the third user --")
user3 = User()
user3.first_name = "Iyanya"
user3.last_name = "Rugger"
user3.email = "dormant@gmail.com"
user3.password = "HeLLo"
