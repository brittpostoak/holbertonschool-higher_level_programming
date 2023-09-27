#!/usr/bin/python3
"""
Function that creates Object from JSON file.
"""
import json


def from_json_string(my_str):
    """
    Begins function - from_json_string.
    """
    return json.loads(my_str)
