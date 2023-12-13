#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import unittest
from models.amenity import Amenity


class TestState(unittest.TestCase):
    """Unittests for testing instantiation of the State class"""

    def setUp(self):
        """Set up State instance for tests"""
        self.instance = Amenity()

    def test_init_attribute_value(self):
        """Check correct init attribute values"""

        name = self.instance.name

        self.assertEqual(name, "")

    def test_set_attribute(self):
        """Check for correct attribute value once set"""

        self.instance.name = "Paris"

        self.assertEqual(self.instance.name, "Paris")


if __name__ == "__main__":
    unittest.main()
