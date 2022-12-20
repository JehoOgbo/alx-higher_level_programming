#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Defines a class for info about a square."""

    def __init__(self, size=0):
        """__init__ initializes the data in the class"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """area - returns the area of the square"""

        return self.__size ** 2
