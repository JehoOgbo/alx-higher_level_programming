#!/usr/bin/python3
"""checks inheritance properties between an object and a class"""


def inherits_from(obj, a_class):
    """ inherits_from: checks if an object is an
        instance of a class that inherited f r o m
        a specified class
        @obj: object to be checked
        @a_class: class in question

        Return: True or False
    """
    if type(obj) == a_class:
        return False
    return (issubclass(type(obj), a_class))
