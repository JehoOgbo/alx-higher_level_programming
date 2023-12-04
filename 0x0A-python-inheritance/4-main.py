#!/usr/bin/python3

is_kind_of_class = __import__('4-inherits_from').inherits_from

a = True
if is_kind_of_class(a, int):
	print("{} is an instance of the class {}".format(a, int.__name__))
if is_kind_of_class(a, bool):
	print("{} is an istance of the class {}".format(a, bool.__name__))
if is_kind_of_class(a, object):
	print("{} is an instance of the class {}".format(a, object.__name__))
