#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    nlen = len(my_list) - 1
    for i in range(nlen, -1, -1):
        print("{}".format(my_list[i]))
