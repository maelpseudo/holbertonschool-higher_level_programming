#!/usr/bin/python3
"""returning the JSON representation of an object"""

import json


def to_json_string(my_obj):
    """define json obj"""
    json_str = json.dumps(my_obj)
    return json_str
