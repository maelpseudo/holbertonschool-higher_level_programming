#!/usr/bin/python3

def new_in_list(my_list, idx, new_element):
    nlen = len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > nlen:
        return my_list
    else:
        updated_list = my_list[:]
        updated_list[idx] = new_element
        return updated_list
