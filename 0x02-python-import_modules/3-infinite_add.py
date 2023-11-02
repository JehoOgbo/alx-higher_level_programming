#!/usr/bin/python3

# This program prints the result of the addition of all command line args
# It should not run when imported

if __name__ == '__main__':
    import sys

    length = (len(sys.argv) - 1)  # length can now exclude argv[0]
    summer = 0
    i = 1

    while i <= length:
        summer += int(sys.argv[i])  # increment the value of the total sum
        i += 1
    print("{:d}".format(summer))  # print the total value
