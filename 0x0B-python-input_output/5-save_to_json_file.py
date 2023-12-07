#!/usr/bin/python3
""" import json module """
import json
""" write an object to a text file using json representation"""


def save_to_json_file(my_obj, filename):
    """ save_to_json_file: changes an object to json text
        then write it to a text file
        Args:
        my_obj: the object to be converted and written
        filename: the name of the file to be written to
    """
    with open(filename, 'w', encoding='utf-8') as openfile:
        openfile.write(json.dumps(my_obj))
