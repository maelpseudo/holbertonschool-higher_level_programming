#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_00_id_increment(self):
        """Test if id is correctly incremented"""
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)

    def test_01_id_assignment(self):
        """Test if the assigned id is correct"""
        base3 = Base(12)
        self.assertEqual(base3.id, 12)

    def test_02_json_string(self):
        """Test converting to JSON string"""
        dictionary = {'id': 10}
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(json_string, '[{"id": 10}]')

    def test_03_json_string_empty(self):
        """Test converting an empty list to JSON string"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_04_json_string_none(self):
        """Test converting None to JSON string"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_05_from_json_string(self):
        """Test converting from JSON string"""
        json_string = '[{"id": 10}]'
        list_output = Base.from_json_string(json_string)
        self.assertEqual(list_output, [{"id": 10}])

    def test_06_from_json_string_empty(self):
        """Test converting an empty JSON string"""
        list_output = Base.from_json_string("")
        self.assertEqual(list_output, [])

    def test_07_from_json_string_none(self):
        """Test converting None to a list"""
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])

# Add more tests as needed

if __name__ == "__main__":
    unittest.main()
