#!/usr/bin/python3
""" MyList inherits from list and adds functionality """


class MyList(list):
    """ class declaration to add sorting to list class """

    def print_sorted(self):
        """ prints a list but sorted (ascending order) all elements int """
        new = self.copy()
        new.sort()
        print(new)
