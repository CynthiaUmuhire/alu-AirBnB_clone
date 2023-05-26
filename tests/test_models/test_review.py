#!/usr/bin/python3
"""
The Unittests for review class
"""
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """Test cases Review class."""

    def test_instance(self):
        """tests instance."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_is_class(self):
        """tests class."""
        review = Review()
        self.assertEqual(str(type(review)),
                         "<class 'models.review.Review'>")

    def test_is_subclass(self):
        """tests subclass."""
        review = Review()
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_text(self):
        """tests text."""
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertEqual(review.text, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.place_id, "")


if __name__ == "__main__":
    unittest.main()