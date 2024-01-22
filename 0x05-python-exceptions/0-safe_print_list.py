#!/usr/bin/python3
# 0-safe_print_list.py
# Bruno Okoth
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count = count + 1
        except IndexError:
            continue
    print("")
    return count
