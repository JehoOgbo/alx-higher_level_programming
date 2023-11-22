#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Defines a class for info about a square"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ initializes the data in the class

        Args:
                size (int): length of a side of square
                position (int, int): position of origin of square
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

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
        if it is an integer greater than 0

        args:
                value: the value to which size is to be set to
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """prints in stdout a square with # characters
        Also prints spaces for the first element of position tuple
        """

        if self.__size == 0:
            print("")
        else:
            row = self.__size

            if self.__position[1] > 0:
                print("\n" * self.__position[1], end='')
            while row > 0:
                print(" " * self.__position[0], end='')
                column = self.__size

                while column > 0:
                    print("#", end='')
                    column -= 1

                print("")
                row -= 1

    @property
    def position(self):
        """returns the value contained in the tuple position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets value for tuple position
        args:
                value: data to be used for setting
                must be tuple of two positive integers
                otherwise, raise typeError
        """

        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
