#!/usr/bin/python3
"""Class to JSON"""
import json


def class_to_json(obj):
    """Class to JSON"""

    obj_dict = {}
    for key, value in vars(obj).items():
        if isinstance(value, (int, dict, str, list, bool)):
            obj_dict[key] = value
    return obj_dict
