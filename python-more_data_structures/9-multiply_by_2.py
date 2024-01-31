#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    a_dictionary_result = a_dictionary.copy()
    for key in a_dictionary_result:
        a_dictionary_result[key] = a_dictionary_result[key] * 2
    return a_dictionary_result
