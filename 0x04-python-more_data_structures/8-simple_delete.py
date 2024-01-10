#!/usr/bin/python3
# 8-simple_delete.py
# Bruno Okoth
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    return a_dictionary
