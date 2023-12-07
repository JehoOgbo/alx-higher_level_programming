#!/usr/bin/python3

""" Appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ append_write: appends string at end of text file
        Args":

        filename - file to which string is added
        text - text to be added
        Return: No of chars appended
    """
    with open(filename, 'a', encoding='utf-8') as openfile:
        # using with ensures the file will close
        chars = openfile.write(text)
    return chars
