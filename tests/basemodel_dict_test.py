import unittest
from models.base_model import BaseModel


class TestBaseModel_to_dict(unittest.TestCase):
    def test_to_dict_return(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(type(base_model_dict), dict)

    def test_to_dict_values(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(type(base_model_dict['created_at']), str)
        self.assertEqual(type(base_model_dict['updated_at']), str)
        self.assertEqual(type(base_model_dict['id']), str)


if __name__ == '__main__':
    unittest.main()
