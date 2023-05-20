#!/usr/bin/python3
"""
Test cases for the city class
"""

import unittest
from models.city import City
from models.state import State
from models.base_model import BaseModel

class test_amenity (unittest.TestCase):
    """Tests the city class"""

def test_instance(self):
    """Tests for intance"""
    object = City()
    self.assertIsInstance(object,City)

def test_subclass(self):
    """Tests if it's a subclass"""
    var = City()
    self.assertTrue(issubclass(type(var), BaseModel))


def name_test(self):
    """name test"""
    var = City()
    self.assertEqual(var.name, "")
    var.name = "Musanze"
    self.assertEqual(var.name, "Musanze")


def test_city_id(self):
    """test city id"""
    city = City()
    self.assertEqual(city.state_id, "")


if __name__ == "__main__":
    unittest.main()
