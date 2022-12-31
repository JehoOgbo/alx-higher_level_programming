#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    prints a string with the name of the person
    Args:
        first_name: name of the person
        last_name: last name of the person
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    string = "My name is"
    print("{:s} {:s} {:s}".format(string, first_name, last_name))
