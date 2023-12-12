#!/usr/bin/python3
"""Defines unittests for models/review.py"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for testing instantiation of the Review class"""

    def setUp(self):
        """Set up Review class instance for tests"""
        self.instance = Review()

    def test_init_attributes(self):
        """Check correct init attribute values"""

        place_id = self.instance.place_id
        user_id = self.instance.user_id
        text = self.instance.text

        self.assertEqual(place_id, "")
        self.assertEqual(user_id, "")
        self.assertEqual(text, "")

    def test_set_attributes(self):
        """Check for correct value once set"""

        self.instance.place_id = "Place.id"
        self.instance.user_id = "User.id"
        self.instance.text = "Host was RUDE!"

        self.assertEqual(self.instance.place_id, "Place.id")
        self.assertEqual(self.instance.user_id, "User.id")
        self.assertEqual(self.instance.text, "Host was RUDE!")


if __name__ == "__main__":
    unittest.main()
