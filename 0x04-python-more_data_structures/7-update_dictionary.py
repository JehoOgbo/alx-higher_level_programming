#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    replace or add key/value in a dictionary
\
    key argument will always be a string
    value argument can be of any type
    If a key already exists in the dictionary, the value will be replaced
    If the key doesn't exist, it will be created
    Do not import any module

    Return the updated dictionary
    """
    if a_dictionary is None:
        a_dictionary = {key: value}
        return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
