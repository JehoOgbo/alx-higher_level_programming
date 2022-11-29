#!/usr/bin/python3
# print numbers from 0 to 99 followed by a comma and a space
for i in range(99):
    print("{:02d}".format(i), end=", ")
print("{:02d}".format(i + 1))
