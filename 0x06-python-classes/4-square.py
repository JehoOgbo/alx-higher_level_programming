#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Defines a class for info about a square"""

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

    @property
    def size(self):
        """returns the size / length of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of the size of the string to value
        if it is an integer greater than 0"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
