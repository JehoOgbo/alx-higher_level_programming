#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
store = number % 10
if store > 5:
	print(f"Last digit of {number:d} is {store:d} and is greater than 5")
elif store == 0:
	print(f"Last digit of {number:d} is {store:d} and is 0")
else:
	print(f"Last digit of {number:d} is {store:d} and is less than 6 and not 0")
