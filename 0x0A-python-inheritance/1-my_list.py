#!/usr/bin/python3
# 1-my_list.py
# Bruno Okoth
# brunookoth44@gmail.com
"""
===========================
Module with class MyList
===========================
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Methot that sorted a list"""

        print(sorted(list(self)))
