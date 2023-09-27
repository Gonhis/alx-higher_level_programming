#!/usr/bin/python3
"""Square class def"""

class Square:
    """ Declare a square class """

    def __init__(self, size=0, position=(0, 0)):
        """
        Intializes the attributes

        Args:
            size: size of square
            position:  position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Gets the private attribute to be used in class """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Define private instance attribute: value
        Raise TypeError & ValueError if not int or <0 resp.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Gets the private attribute to be used in class """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Function that sets position of the square
        Raise TypeError if value is not tuple or value !=2 or <0
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value     # tuple contains 2 positive integers

    def area(self):
        """ Return area of a square """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            i = 0
            pos1, pos2 = self.__position
            for new_line in range(pos2):
                print()
            while i < self.__size:

                c = 0
                while c < pos1:
                    print(" ", end='')  # replace position with space
                    c += 1

                j = 0
                while j < self.__size:
                    print("{}".format("#"), end='')
                    j += 1
                print()
                i += 1
