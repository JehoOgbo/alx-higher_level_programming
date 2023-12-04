#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class Myclass(object):
    pass

class Myclass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(Myclass))
print(lookup(Myclass2))
print(lookup(int))
