#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return None

    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    i = 0

    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_numerals[roman_string[i]] < roman_numerals[roman_string[i + 1]]:
            result += roman_numerals[roman_string[i + 1]] - roman_numerals[roman_string[i]]
            i += 2
        else:
            result += roman_numerals[roman_string[i]]
            i += 1

    return result
