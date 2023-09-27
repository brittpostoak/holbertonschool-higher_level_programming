#!/usr/bin/python3
"""
Function that returns JSON representation of an object.
"""


def to_json_string(my_obj):
    """Begins function - to json string"""
    import json
    return json.dumps(my_obj, ensure_ascii=False)
