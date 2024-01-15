#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """Inherits from or not"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
