#!/usr/bin/python3
"""
A module that defines a class
"""


class Square:
    """
    A Class that defines a square
    """

    def __init__(self, size=0):
        """
        args:
            size = defines the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
