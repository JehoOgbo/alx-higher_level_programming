#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """ is_kind_of_class: checks if an object is an instance
        of a class or of one which inherits f r o m that class
        @obj: object in question
        @a_class: class which object might inherit f r o m
    """
    if type(obj) == a_class:
        return True
    return issubclass(type(obj), a_class)
