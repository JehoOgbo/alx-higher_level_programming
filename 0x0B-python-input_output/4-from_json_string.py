#!/usr/bin/python3
""" import the json module """
import json
""" returns an object represented by a json string """


def from_json_string(my_str):
    """ from_json_string: changes a json string to an object """
    return json.loads(my_str)
