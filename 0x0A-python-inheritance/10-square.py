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


"""A class that inherits some methods. Parentclass: BaseGeometry"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """initializes the object"""
        BaseGeometry.__init__(self)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area: Finds the area of a rectangle
            takes no arguments as it uses
            private instance attributes
        """
        return (self.__width * self.__height)

    def __str__(self):
        """__str__: defines what is printed when
           print is used on the class
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


""" A grandchild class with parent
    Rectangle and grandparent BaseGeometry
"""


class Square(Rectangle):
    def __init__(self, size):
        """initializes the square with the length of its sides"""
        Rectangle.__init__(self, size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area: Returns the area of the square"""
        return (self.__size ** 2)
