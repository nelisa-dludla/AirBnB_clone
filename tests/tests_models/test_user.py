#!/usr/bin/python3
"""Defines unittests for models/user.py"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for testing instantiation of the User class"""

    def setUp(self):
        """Set up User instance for tests"""
        self.instance = User()

    def test_init_attributes(self):
        """Check correct init attribute values"""

        email = self.instance.email
        password = self.instance.password
        first_name = self.instance.first_name
        last_name = self.instance.last_name

        self.assertEqual(email, "")
        self.assertEqual(password, "")
        self.assertEqual(first_name, "")
        self.assertEqual(last_name, "")

    def test_set_attributes(self):
        """Check for correct attribute values once set"""

        self.instance.email = "johndoe@gmail.com"
        self.instance.password = "qwerty"
        self.instance.first_name = "John"
        self.instance.last_name = "Doe"

        self.assertEqual(self.instance.email, "johndoe@gmail.com")
        self.assertEqual(self.instance.password, "qwerty")
        self.assertEqual(self.instance.first_name, "John")
        self.assertEqual(self.instance.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
