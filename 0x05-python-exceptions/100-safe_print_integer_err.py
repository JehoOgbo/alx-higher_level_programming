#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    """
    prints an integer stored in value

    value: may contain an integer

    Return: true if value has been printed false otherwixe
    then print error on stderr
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as ex:
        stderr.write("Exception: {}\n".format(ex.args[0]))
        return False
    else:
        return True
