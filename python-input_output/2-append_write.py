#!/usr/bin/python3
"""appending a string at the end of a text file"""


def append_write(filename="", text=""):
    """write file"""
    with open(filename, 'a', encoding='UTF8') as file:
        file.write(text)
    chars = len(text)
    return chars
