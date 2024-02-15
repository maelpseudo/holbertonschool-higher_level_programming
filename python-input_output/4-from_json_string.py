#!/usr/bin/python3
"""returning an object from JSON representation"""

import json


def from_json_string(my_str):
    """define json obj"""
    obj = json.loads(my_str)
    return obj
