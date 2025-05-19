#!/usr/bin/python3
"""A class that inherits some methods. Parentclass: BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class with some methods"""

    def __init__(self, width, height):
        """initializes the object"""
        BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
