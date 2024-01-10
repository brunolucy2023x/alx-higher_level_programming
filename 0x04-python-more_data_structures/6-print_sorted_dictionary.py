#!/usr/bin/python3
# 6-print_sorted_dictionary.py
# Bruno Okoth
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
