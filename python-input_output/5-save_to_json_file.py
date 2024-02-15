#!/usr/bin/python3
"""import json module"""

import json


def save_to_json_file(my_obj, filename):
    """Write the JSON string to a text file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
