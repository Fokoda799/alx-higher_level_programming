#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """Is kind of class or not"""
    if isinstance(obj, a_class):
        return True
    return False
