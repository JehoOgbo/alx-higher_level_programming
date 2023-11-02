#!/usr/bin/python3

# This program prints all names defined in a compiled module hidden_4.pyc

if __name__ == '__main__':
    import hidden_4
    for i in dir(hidden_4):
        if i[:2] != "__":
            print("{}".format(i))
