#!/usr/bin/python3
# 2-replace_in_list.py
# Bruno Okoth
def replace_in_list(my_list, idx, element):
    listlength = len(my_list) - 1
    if (idx < 0 or idx > listlength):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
