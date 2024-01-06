#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Bruno Okoth
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for number in my_list:
            print("{:d}".format(number))
