#!/usr/bin/python3
# 4-inherits_from.py
# Bruno Okoth
# brunookoth44@gmail.com
"""
===================================
module with method inherits_from
===================================
"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
