#!/usr/bin/python3
# prints a string in uppercase followed by a new line
def uppercase(str):
    new = str
    for i in new:		# iterate through all the chars in the word
        num = ord(i)	# get the ascii equivalent of each character
        char = i		# store the char in a new variable
        if (num >= 97) and (num <= 122):  # if lower, assign uppercase value
            char = chr(num - 32)
        print("{:s}".format(char), end='')	# print the char
    print("")				# print terminating newline character
