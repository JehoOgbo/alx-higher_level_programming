#!/usr/bin/python3
""" a class that inherits from int """


class MyInt(int):
    """ This class inherits from int but rebels """
    def __eq__(self, other):
        """ tests if a number is not equal to another """
        return super().__ne__(other)

    def __ne__(self, other):
        """ tests if the numbers are equal to each other """
        return super().__eq__(other)
