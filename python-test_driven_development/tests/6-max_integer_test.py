#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with the max integer at the beginning"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_one_element_list(self):
        """Test with a list that contains one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative_integers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_same_elements(self):
        """Test with a list where all elements are the same"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_with_floats_and_integers(self):
        """Test with a list containing both floats and integers"""
        self.assertEqual(max_integer([1.1, 2, 3.3, 4]), 4)

    def test_with_strings(self):
        """Test raising a TypeError with a list containing strings"""
        with self.assertRaises(TypeError):
            max_integer(["Hello", "world"])
