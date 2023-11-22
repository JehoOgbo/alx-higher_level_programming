#!/usr/bin/python3

"""Docstring for class Node"""


class Node:
    """Defines the node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """__init__ initializes the data in the node
        Args:
            data: data to be used to set data
            next_node: the next node of the list
        Cause an exception if data is not of type int
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

        if type(next_node) is not object and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """retuns the data stored in data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data to be stored in data.
        Args:
            value: value to be used to set data
        Causes an exception if value is not of type int
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves data for next node of list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the data for the next node
        Args:
            value: data of the next node in the list
        raise an exception if value is not a node object or none
        """
        if type(next_node) is not object and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node



""" Docstring for class SinglyLinkedList"""


class SinglyLinkedList:
    """SinglyLinkedList - class for singlyLinked list operations"""
    def __init__(self):
        self.__head = None
    def sorted_insert(self, value):
        """Insets a new Node into list in increasing order
        Args:
            value: value to be added to list
        """
        new = Node(value, None)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self._head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                   tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define print representation of a singly linked list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
