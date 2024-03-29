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

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a student"""
        if type(attrs) is not list:
            return self.__dict__
        for item in attrs:
            if type(item) is not str:
                return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """ replaces all attributes of the student instance
        Args:
            json: dictionary containing new descriptions for
                  the attributes
        """
        for key in json:
            if hasattr(self, key):
                setattr(self, key, json[key])
