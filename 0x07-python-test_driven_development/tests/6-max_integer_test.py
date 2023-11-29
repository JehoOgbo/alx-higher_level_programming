#!/usr/bin/python3
'''Unittest for max_integer([..])
'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TextMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])"""

    def test_empty_list(self):
        """Test empty list"""
        self.assertEqual(max_integer([]), None)

    def test_values(self):
        """Test unordered values"""
        self.assertEqual(max_integer([2, 4, 8, 90, 63, 9]), 90)

    def test_ints_and_floats(self):
        """Test a list of ints and floats"""
        self.assertEqual(max_integer([2.43, 5, 83.53, 3533]), 3533)

    def test_strings(self):
        """Test a string. Returns char with highest ascii values"""
        self.assertEqual(max_integer("Brittany"), 'r')

    def test_list_of_strings(self):
        """Test a list of string.
        Returns string whose first char has highest ascii value
        """
        self.assertEqual(max_integer(["Brennan", "is", "my", "name"]), "name")

    def test_empty_string(self):
        """Test an empty string. Returns None"""
        self.assertEqual(max_integer(''), None)

    def test_one_element(self):
        """Test a list with single element"""
        self.assertEqual(max_integer([8]), 8)
