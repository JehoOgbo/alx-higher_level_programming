#!/usr/bin/python3
""" Adds all arguments to a python list and save them to a file """
import sys
save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file


def add_item(argv):
    """
    add_item: adds all command line arguments to a list

    Args:
    argv: argument vector containing command line arguments
    """
    # check if the file already exits
    # if so load the list inside
    # else create a new list
    try:
        new_list = load_from("add_item.json")
    except FileNotFoundError:
        new_list = []
    i = 0
    while i < len(argv):
        if i != 0:
            new_list.append(argv[i])
        i += 1
    # items.extend(sys.argv[1:]) also possible
    return new_list

if __name__ == '__main__':
    my_list = add_item(sys.argv)
    save_to(my_list, "add_item.json")
