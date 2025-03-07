#!/usr/bin/python3
"""
Module Square
"""


class Square:
    """
    Square class representing a geometric shape.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square in a 2D space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square class.

        Args:
            size (int): The size of the square, must be a non-negative integer.
            position (tuple): A tuple of two positive integers representing the position.

        Raises:
            TypeError: If size is not an integer or position is not a tuple of two positive integers.
            ValueError: If size is negative.
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square in a 2D space.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print the square using '#' characters considering position.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
