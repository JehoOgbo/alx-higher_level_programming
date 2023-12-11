#!/usr/bin/python3
import unittest
from models.base import Base
""" tests the class base"""


class TestBase(unittest.TestCase):
    """ Define unittests for class Base"""

    b = Base()

    def test_nb_objects_is_private(self):
        """ tests to see that __nb_object is a private class attribute"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_priv_attr_increments(self):
        """ tests to see that the private instance attribute works """
        new = Base()
        self.assertEqual(1, TestBase.b.id)  # increases by one if no args
        self.assertEqual(15, Base(15).id)  # isn't used if id is provided

    def test_args_or_no_args(self):
        """ tests what happens if args are provided or not"""
        self.assertEqual(15, Base(15).id)  # arg is assigned to id
        self.assertTrue(Base().id)  # if no arg id is given a value anyway

    def test_type_of_arg(self):
        """ tests what happens if args of different types are passed
            Should work no matter type of args passed
        """
        new_test = Base("str")
        this = Base(True)
        fin = Base(None)
        loaf = Base(8.77)
        other = Base(chr(69))
        self.assertEqual(15, Base(15).id)
        self.assertEqual(True, this.id)
        self.assertEqual(8.77, loaf.id)
        self.assertEqual('E', other.id)
        self.assertTrue(fin.id)  # in case of None, works as with no args

    def test_more_than_one_argument(self):
        """ Checks what happens if there are too many args"""
        with self.assertRaises(TypeError):
            Base(34, 45)


if __name__ == '__main__':
    unittest.main()
