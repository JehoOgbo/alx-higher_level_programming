#!/usr/bin/python3
""" class that defines a student """


class Student:
    """ This is a class that defines a student by their
        firstname, lastname and age
    """

    def __init__(self, first_name, last_name, age):
        """ Initialize the class with info about the student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a student"""
        return self.__dict__
