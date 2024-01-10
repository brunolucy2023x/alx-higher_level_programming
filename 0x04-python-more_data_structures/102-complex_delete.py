#!/usr/bin/python3
# 102-complex_delete.py
# Bruno Okoth
def complex_delete(a_dictionary, value):
    for k, v in list(a_dictionary.items()):
        if v is value:
            a_dictionary.pop(k)
    return a_dictionary
