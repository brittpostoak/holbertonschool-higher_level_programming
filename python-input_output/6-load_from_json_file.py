#!/usr/bin/python3
"""
Function that creates Object from JSON file.
"""
import json


def load_from_json_file(filename):
    """Begins function - load from json"""
    import json
    with open(filename, "r") as file:
        return json.load(file)
