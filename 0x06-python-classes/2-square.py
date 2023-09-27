#!/usr/bin/python3
"""Square class defination."""


class Square:
    """declare a square class"""

    def __init__(self, size=0):
        """
        Define private instance attribute: size
        Raise TypeError & ValueError if not int or <0 .
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
