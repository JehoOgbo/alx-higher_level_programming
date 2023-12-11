#!/usr/bin/python3
import unittest
from models.base import Base
""" tests the class base"""


class TestBase:
    """ Define unittests for class Base"""

    def setUp(self):
        """ sets up the environment for each of the tests"""
        tester = Base()
        see = Base(15)

    def tearDown(self):
        """ tears down set up code after each test"""
        tester = None

    def test_nb_objects_is_private(self):
        """ tests to see that __nb_object is a private class attribute"""
        with self.assertRaises(AttributeError):
            print(tester.__nb_objects)

    def test_priv_attr_increments(self):
        """ tests to see that the private instance attribute works """
        new_test = Base()
        seer = Base(None)
        self.assertEqual(1, tester.id)  # iniitally increases to one
        self.assertEqual(2, new_test.id)  # keeps incrementing
        self.assertEqual(15, see.id)  # isn't used if id is provided
        self.assertEqual(3, seer.id)  # continues working otherwise

    def test_args_or_no_args(self):
        """ tests what happens if args are provided or not"""
        self.assertEqual(15, see.id)  # arg is assigned to id
        self.assertTrue(tester.id)  # if no arg id is given a value anyway

    def test_type_of_arg(self):
        """ tests what happens if args of different types are passed
            Should work no matter type of args passed
        """
        new_test = Base("str")
        this = Base(True)
        fin = Base(None)
        loaf = Base(8.77)
        other = Base(chr(9))
        self.asserEqual(15, see.id)
        self.assertEqual(True, this.id)
        self.assertEqual(8.77, loaf.id)
        self.assertEqual('E', other.id)
        self.assertEqual(2, fin.id)  # in case of None, works as with no args
