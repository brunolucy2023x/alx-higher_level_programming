#!/usr/bin/python3
# 1-square.py
# brunookoth44@gmail.com
# Bruno Okoth
"""Describes and explains a class Square"""


class Square:
    """
    Class that descibes and explains  properties of square by: (based on 0-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size):
        """Forms new instances of square (1 side).

        Args:
            size: size of the square.
        """
        self.__size = size
