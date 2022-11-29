#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    string = "negative"
elif number == 0:
    string = "zero"
elif number > 0:
    string = "positive"
print(f"{number:d} is {string}")		# print message
