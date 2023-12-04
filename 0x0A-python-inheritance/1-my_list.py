#!/usr/bin/python3

""" Mylist: subclass which inherits. Parentclass: list
    @list: superclass
"""


class MyList(list):
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        """ print_sorted: function that sorts the contents
            of a list in ascending order then prints the list
            Assumes every element of the list will be an integer
        """
        new = []
        for item in self:
            new.append(item)
        num = len(self)
        i = 0
        while i < num:
            j = i + 1
            while j < num:
                if new[i] > new[j]:
                    hold = new[i]
                    new[i] = new[j]
                    new[j] = hold
                j += 1
            i += 1

        print(new)
