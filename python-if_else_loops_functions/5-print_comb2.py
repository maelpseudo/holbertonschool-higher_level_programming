#!/usr/bin/python3

for i in range(0, 100):
    if i < 99:
        comma = ","
        if i < 10:
            digit = "0"
        else:
            digit = ""
    else:
        comma = ""
    print("{0}{1}{2}".format(digit, i, comma), end=" ")
print("\n", end="")
