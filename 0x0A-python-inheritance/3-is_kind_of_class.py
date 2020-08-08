#!/usr/bin/python3
""" is_kind_of_class function  """


def is_kind_of_class(obj, a_class):
"""
obj = object
a_class = class
"""
    if isinstance(obj, a_class):
        return True
    return False
