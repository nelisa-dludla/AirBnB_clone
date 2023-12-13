#!/usr/bin/python3
"""Defines unittests for models/state.py"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unittests for testing instantiation of the State class"""

    def setUp(self):
        """Set up State instance for tests"""
        self.instance = State()

    def test_init_attribute_value(self):
        """Check correct init attribute values"""

        name = self.instance.name

        self.assertEqual(name, "")

    def test_set_attribute(self):
        """Check for correct attribute value once set"""

        self.instance.name = "Alx"

        self.assertEqual(self.instance.name, "Alx")


if __name__ == "__main__":
    unittest.main()
