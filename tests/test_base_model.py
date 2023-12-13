#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines unittests for the BaseModel class"""

    def setUp(self):
        """Create an instance of BaseModel to used in tests"""

        self.instance = BaseModel()
        instance_dict = self.instance.to_dict()
        self.instance2 = BaseModel(**instance_dict)

    def test_id_type(self):
        """Check the type of id"""

        result = self.instance.id
        self.assertEqual(type(result), str)

    def test_created_at_type(self):
        """Check the type of created_at"""

        result = self.instance.created_at
        self.assertEqual(type(result), datetime)

    def test_updated_at_type(self):
        """Check the type of updated_at"""

        result = self.instance.updated_at
        self.assertEqual(type(result), datetime)

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("bigdata.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updated_updated_at(self):
        """Check updated_at value after save is executed"""

        current_value = self.instance.updated_at
        new_value = self.instance.save()

        self.assertNotEqual(current_value, new_value)

    def test_id_type_kwargs(self):
        """Check the type of id"""

        result = self.instance2.id
        self.assertEqual(type(result), str)

    def test_created_at_type_kwargs(self):
        """Check the type of created_at"""

        result = self.instance2.created_at
        self.assertEqual(type(result), datetime)

    def test_updated_at_type_kwargs(self):
        """Check the type of updated_at"""

        result = self.instance2.updated_at
        self.assertEqual(type(result), datetime)

    def test_to_dict_return_type(self):
        """Check the type of return value"""

        result = self.instance.to_dict()
        self.assertEqual(type(result), dict)

    def test_to_dict_return_keys(self):
        """Check key values of dict returned"""

        keys = self.instance.to_dict().keys()

        self.assertIn("id", keys)
        self.assertIn("updated_at", keys)
        self.assertIn("created_at", keys)
        self.assertIn("__class__", keys)

    def test_to_dict_created_at_format(self):
        """Check created_at format is isoformat"""

        result_dict = self.instance.to_dict()
        result = result_dict["created_at"]
        expected_output = self.instance.created_at.isoformat()

        self.assertEqual(result, expected_output)

    def test_to_dict_updated_at_format(self):
        """Check updated_at format is isoformat"""

        result_dict = self.instance.to_dict()
        result = result_dict["updated_at"]
        expected_output = self.instance.updated_at.isoformat()

        self.assertEqual(result, expected_output)

    def test_str(self):
        """Check str representation"""

        id = self.instance.id
        instance_dict = self.instance.__dict__
        result = str(self.instance)
        expected_output = f"[BaseModel] ({id}) {instance_dict}"

        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
