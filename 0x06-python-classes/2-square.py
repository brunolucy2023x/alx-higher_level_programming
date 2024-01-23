#!/usr/bin/python3
# 2-square.py
# brunookoth44@gmail.com
# Bruno Okoth
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 1-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """generates fresh square instances.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("Size needs to be a whole number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
