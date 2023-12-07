#!/usr/bin/python3

"""Writes a string to a file and return no. of chars written"""


def write_file(filename="", text=""):
    """ write_file: writes a string to a file

        Args:
        filename - the name of the file to be written to
        text - the information to be written

        Return: the number of characters written
    """
    with open(filename, "w", encoding='utf=8') as openfile:
        chars = openfile.write(text)
    return chars
