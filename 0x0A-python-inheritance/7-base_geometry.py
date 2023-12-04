#!/usr/bin/python3

"""A class with public instance method which raises an exception"""


class BaseGeometry():
    def __init__(self):
        """initializes the object"""
        pass

    def area(self):
        """ area: Public instance method which raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator: Public instance meethod that ensures
            value is an integer and positive
            @name: name of the shape (always a string)
            @value: value to be validated

            Exceptions ValueError and TypeError to be raised if
            value is not validated
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
