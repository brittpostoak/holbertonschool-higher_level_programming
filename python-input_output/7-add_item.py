#!/usr/bin/python3
"""
Script that adds all arguments to list then saves them to file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Begins function - Save to json.
    """
    with open(filename, encoding='utf-8', mode='w') as f:
        f.write(json.dumps(my_obj))
