#!/usr/bin/python3

"""This function reads a text file and prints it to stdout"""


def read_file(filename=""):
    """ read_file: reads a textfile and print its contents
        Args:
        filename: The name of the textfile to be read
    """
    with open(filename, encoding='utf-8') as openfile:
        read_file = openfile.read()
    print(read_file, end="")
