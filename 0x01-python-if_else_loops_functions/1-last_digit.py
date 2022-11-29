#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    last = 0
elif number > 0:
    last = number % 10
else:
    last = -number % 10
    last = -last
if last > 5:
    string = "and is greater than 5"
elif last == 0:
    string = "and is 0"
elif last < 6:
    string = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {:s}".format(number, last, string))
