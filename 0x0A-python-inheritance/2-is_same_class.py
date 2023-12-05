#!/usr/bin/pyhon3
"""Returns true or false if an object is an exact instance of a class"""


def is_same_class(obj, a_class):
    """ is_same_class: This function checks if an object
        is an instance of a class.
        @obj: object to be checked
        @a_class: class to be checked

        Return: True if object and false otherwise
    """
    if type(obj) == a_class:
        return True
    return False
