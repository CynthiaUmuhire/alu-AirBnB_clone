#!/usr/bin/python3
"""
Test cases for the amenity class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class test_amenity (unittest.TestCase):
    """Tests the amenty class"""

def test_instance(self):
    """Tests for intance"""
    object = Amenity()
    self.assertIsInstance(object,Amenity)

def test_subclass(self):
    """Tests if it's a subclass"""
    var = Amenity()
    self.assertTrue(issubclass(type(var), BaseModel))


def name_test(self):
    """name test"""
    var = Amenity()
    self.assertEqual(var.name, "")
    var.name = "Hi"
    self.assertEqual(var.name, "Hi")
    self.assertIsNotNone(var.id)


if __name__ == "__main__":
    unittest.main()
#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
