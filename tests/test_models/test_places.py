#!/usr/bin/python3
"""
Test cases for the city class
"""

import unittest
from models.user import User
from models.place import Place
from models.city import  City
from models.amenity import Amenity
from models.base_model import BaseModel

class test_amenity (unittest.TestCase):
    """Tests the place class"""

def test_instance(self):
    """Tests for intance"""
    object = Place()
    self.assertIsInstance(object,Place)

def test_subclass(self):
    """Tests if it's a subclass"""
    var = Place()
    self.assertTrue(issubclass(type(var), BaseModel))
                           

def test_is_attr(self):
        """test instance."""
        city = City()
        user = User()
        place = Place()
        place.user_id = user.id
        place.city_id = city.id
        self.assertIsNotNone(place.id)
        self.assertEqual(place.user_id, user.id)
        self.assertEqual(place.city_id, city.id)
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0)
        self.assertEqual(place.longitude, 0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
