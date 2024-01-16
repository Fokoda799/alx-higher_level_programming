#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Save Object to a file"""

    with open(filename, 'w') as file:
        return json.dump(my_obj, file, indent=2)
