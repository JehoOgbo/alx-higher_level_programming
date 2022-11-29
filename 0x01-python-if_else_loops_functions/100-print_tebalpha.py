#!/usr/bin/python3

i = 122
j = 1
while i >= 97:
    if j % 2 == 0:
        i = i - 32
    print("{}".format(chr(i)), end="")
    if j % 2 == 0:
        i = i + 32
    j = j + 1
    i = i - 1
