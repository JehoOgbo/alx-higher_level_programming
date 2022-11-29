#!/usr/bin/python3
# print numbers from 0 to 99 followed by a comma and a space
for i in range(100):
    if (i == 99):
        print("{}".format(i))
    else:
        print("{:02d}, ".format(i), end='')
