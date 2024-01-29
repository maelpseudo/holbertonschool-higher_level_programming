#!/usr/bin/python3

def replace_in_list(my_list, idx, new_element):
    nlen = len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > nlen:
        return my_list
    else:
        my_list[idx] = new_element
        return (my_list)
