#!/usr/bin/python3
# 1-safe_print_integer.py
# Bruno Okoth
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except BaseException:
        return False
