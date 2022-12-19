#!/usr/bin/python3
def safe_print_integer(value):
    """
    prints an integer
    value can be any type
    The integer should be printed followed by a new line
    Return True if value has been correctly printed otherwise false
    You have to use try: / execpt:
    Use "{:d}". format
    Do not import any module
    Do not use type()
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
