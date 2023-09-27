#!/usr/bin/python3
"""
Function that writes Object to text file using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Begins function - save to json"""
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj, ensure_ascii=False))
