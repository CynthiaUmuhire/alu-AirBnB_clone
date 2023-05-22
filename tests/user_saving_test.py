#!/usr/bin/python3
"""Testing user saving"""

from models import storage
from models.user import User

def print_all_objects():
    """Prints all the objects in the storage"""
    all_objs = storage.all()
    print("__Reloaded objects__")
    for obj_id, obj in all_objs.items():
        print(obj)

def create_user(first_name, last_name, email, password):
    """Creates a new User instance"""
    user = User()
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.password = password
    return user

def main():
    """Main function"""
    print_all_objects()

    print("-- Create the first user --")
    user1 = create_user("Nate", "DUNKAN", "Ndunkan@gmail.com", "L.o.v.e")
    storage.save()

    print("-- Create the second user --")
    user2 = create_user("Kristina", "Michaelson", "kristina@gmail.com", "come")
    storage.save()

    print("-- Create the third user --")
    user3 = create_user("Iyanya", "Rugger", "dormant@gmail.com", "HeLLo")
    storage.save()

    print_all_objects()

if __name__ == '__main__':
    main()
