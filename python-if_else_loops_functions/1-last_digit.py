#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])
if lastdigit > 5:
    str = "and is greater than 5"
elif lastdigit < 6 and lastdigit > 0:
    str = "and is less than 6 and not 0"
else :
    str = "and is 0"

print(f"Last digit of {number} is {lastdigit} {str}")
