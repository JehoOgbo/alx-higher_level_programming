#!/usr/bin/python3
"""import the json module """
import json
"""create an object from a JSON file """


def load_from_json_file(file_name):
    """
    load_from_json_file: reads a json file and use the data to
    create an object
    Args:

    file_name: name of file which contains the json objects
    """
    with open(file_name, 'r', encoding='utf-8') as openfile:
        new = openfile.read()
    return json.loads(new)
