#!/usr/bin/python3
# program to print all possible different combinations of two numbers
for i in range(8):						# first loop to go through 0 to 7
    for j in range(i + 1, 10):			# 2nd loop goes from 1 digit + 1 to 10
        print("{:d}{:d}".format(i, j), end=", ")		# print both numbers
print("{:d}{:d}".format(i + 1, j))		# print the last number
