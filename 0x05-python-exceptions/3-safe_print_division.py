#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Assume a and b are integers
    print the result in finally section
    preceeded by INside result:
    Returns value of division otherwise None
    Use try: / except: / finally:
    Use str.format
    Do not import any module
    """
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
