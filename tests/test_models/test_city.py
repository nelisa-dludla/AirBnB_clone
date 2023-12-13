#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        """Checks for arg instances"""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """Checks if new instance is in storage"""
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Checks if id is a string"""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Checks that created_at is a public attribute"""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """Checks that updated_at is a public attribute  """
        self.assertEqual(datetime, type(City().updated_at))

    def test_two_cities_unique_ids(self):
        """Checks that two instances have different ids"""
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        """Compares two created_at datetime objects"""
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        """Compares two updated_at datetime objects """
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_city_attributes(self):
        """Tests the city class with values"""
        ct = City()
        ct.name = "Ohio"
        ct.state_id = "121221"
        ctstr = ct.to_dict()
        self.assertEqual("Ohio", ctstr["name"])
        self.assertEqual("121221", ctstr["state_id"])

    def test_str_representation(self):
        """Test city instance with below attributes """
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_instantiation_with_kwargs(self):
        """Checks instances with kwargs"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    def test_to_dict_type(self):
        """Checks for correct dict type"""
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Checks if instance contains correct keys"""
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Checks for added attributes"""
        cy = City()
        cy.middle_name = "Holberton"
        cy.my_number = 98
        self.assertEqual("Holberton", cy.middle_name)
        self.assertIn("my_number", cy.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Checks that datetime attributes are strs"""
        cy = City()
        cy_dict = cy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_args_unused(self):
        """Tests when None is passed"""
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_to_dict_output(self):
        """Compares dict of instance with created tdict"""
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    def test_attribute(self):
        """Tests if attribute works"""
        instance = City()
        instance.name = "Paris"
        instance.state_id = "State.id"

        self.assertEqual(instance.name, "Paris")
        self.assertEqual(instance.state_id, "State.id")


if __name__ == "__main__":
    unittest.main()
