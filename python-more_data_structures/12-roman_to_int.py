#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Mapping of Roman numerals to their integer values
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    result = 0
    prev_value = 0

    # Iterate over the string in reverse order
    for char in reversed(roman_string):
        value = roman_numerals[char]
        if value < prev_value:
            # If the current value is less than the previous one, subtract it
            result -= value
        else:
            # Otherwise, add the current value
            result += value
        prev_value = value

    return result
