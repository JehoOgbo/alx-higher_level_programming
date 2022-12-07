#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    deletes a key in a dictionary
    key argument will always be a string
    If the key doesn't exist, the dictionary won't change

    Do not import any module
    Return: a new dictionary
    """
    if a_dictionary is None:
        return None
    if key in a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary
