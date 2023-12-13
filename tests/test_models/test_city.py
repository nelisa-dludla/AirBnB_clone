#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import unittest
from models.city import City


class TestState(unittest.TestCase):
    """Unittests for testing instantiation of the State class"""

    def setUp(self):
        """Set up State instance for tests"""
        self.instance = City()

    def test_init_attribute_value(self):
        """Check correct init attribute values"""

        state_id = self.instance.state_id
        name = self.instance.name

        self.assertEqual(state_id, "")
        self.assertEqual(name, "")

    def test_set_attribute(self):
        """Check for correct attribute value once set"""

        self.instance.name = "Paris"
        self.instance.state_id = "State.id"

        self.assertEqual(self.instance.name, "Paris")
        self.assertEqual(self.instance.state_id, "State.id")


if __name__ == "__main__":
    unittest.main()
