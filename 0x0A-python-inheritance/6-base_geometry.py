#!/usr/bin/python3

"""A class with public instance method which raises an exception"""


class BaseGeometry():
    def __init__(self):
        """initializes the object"""
        pass

    def area(self):
        """ Public instance method which raises an exception"""
        raise Exception("area() is not implemented")
