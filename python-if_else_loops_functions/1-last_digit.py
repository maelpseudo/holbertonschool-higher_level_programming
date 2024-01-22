#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if int(repr(number)[-1]) > 5:
    str = "and is greater than 5"
elif int(repr(number)[-1]) < 6:
    str = "and is less than 6 and not 0"
else:
    str = "and is 0"

print(f"the last digit of {number} is {int(repr(number)[-1])} {str}")
