#!/usr/bin/python3
# prints a string in uppercase followed by a new line
def uppercase(str):
    """Print a string in uppercase."""
    for i in str:  # iterate through all the chars in the word
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end='')
    print('')
