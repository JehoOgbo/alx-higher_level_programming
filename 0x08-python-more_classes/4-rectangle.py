#!/usr/bin/python3

"""Defines a rectangle"""


class Rectangle:
    """defines a simple rectangle"""
    def __init__(self, width=0, height=0):
        """initialize values width and height of rectangle"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """return perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """define string representation of the class"""
        if self.width == 0 or self.height == 0:
            return ("")
        for i in range(0, self.__height):
            [print("#", end='') for j in range(0, self.__width)]
            if i != self.__height - 1:
                print("")
        return ("")

    def __repr__(self):
        """return a string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width) + ', ' + str(self.__height)
        rect += ')'
        return rect
