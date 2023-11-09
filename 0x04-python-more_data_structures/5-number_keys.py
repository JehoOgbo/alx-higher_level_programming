#!/usr/bin/python3
def number_keys(a_dictionary):
    """ Returns the number of keys in a dictionary """
    if a_dictionary is None:
        return 0
    num_of_keys = 0
    for i in a_dictionary:
        num_of_keys += 1
    return (num_of_keys)
