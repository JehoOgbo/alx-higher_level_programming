#!/usr/bin/python3

# prints number of command line arguments as well as all the arguments


if __name__ == '__main__':
    import sys

    length = (len(sys.argv) - 1)
    string = "arguments"
    i = 1

    if length == 0:
        print("{} {}.".format(length, string))
        sys.exit()
    if length == 1:
        print("{} {}:".format(length, string[:8]))
    else:
        print("{} {}:".format(length, string))
    while i <= length:
        print("{}: {}".format(i, sys.argv[i]))
        i = i + 1
