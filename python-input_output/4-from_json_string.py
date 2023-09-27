#!/usr/bin/python3
"""
Function that returns object represented by a JSON string.
"""


def from_json_string(my_str):
    """Begins function - from json string"""
    import json
    return json.loads(my_str)
