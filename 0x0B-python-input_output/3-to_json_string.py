#!/usr/bin/python3

""" Import module JSON"""
import json
""" returns the json reprensentation of an object"""


def to_json_string(my_obj):
    """ to_json_string: returns json representation of the object
        Args:
        my_obj - object to be converted to json string
    """
    return json.dumps(my_obj)
