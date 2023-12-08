#!/usr/bin/python3
""" returns the dictionary desc with simple data structure
    for JSON serialization of an object
"""


def class_to_json(obj):
    """
    class_to_json: returns dict desc with simple data structure
    for JSON serialization of an object
    Args:

    obj: instance of a class
    note: all attributes of a class are serializable
    """
    return (obj.__dict__)
