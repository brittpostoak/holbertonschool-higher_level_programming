#!/usr/bin/python3
"""
Function that writes Object to text file using a JSON representation.
"""
import json


def to_json_string(my_obj):
    """
    Begins function - to_json_string.
    """
    return json.dumps(my_obj)
