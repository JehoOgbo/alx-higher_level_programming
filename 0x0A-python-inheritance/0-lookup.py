#!/usr/bin/python3
"""Defines a list of an object's available attributes"""


def lookup(obj):
    """This function returns a list
    of available attributes and
    methods of an object"""
    return (dir(obj))
