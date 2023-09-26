#!/usr/bin/python3
"""Square class defination"""
class Square:
    """ Declare a square class """

    def __init__(self, size=0):
        """
        Intializes the attributes

        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """ Gets the attribute to be used in class """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Define private instance attribute: value
        Raise TypeError & ValueError if not int or <0 .
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Return  area of a square """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            i = 0
            while i < self.__size:
                j = 0
                while j < self.__size:
                    print("{}".format("#"), end='')
                    j += 1
                print()
                i += 1
