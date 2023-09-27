#!/usr/bin/python3
"""
Function that returns dictionary description with data 
structure for JSON serialization of object.
"""
import json


def load_from_json_file(filename):
    """
    Begins function - load from json object.
    """
    with open(filename, encoding='utf-8', mode='r') as f:
        text = f.read()
        return json.loads(text)
