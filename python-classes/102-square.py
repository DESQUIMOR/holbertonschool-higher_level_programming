#!/usr/bin/python3
"""
Module for defining a Square class.
"""


class Square:
    """
    Defines a square with size attributes and comparison methods.
    """

    def __init__(self, size=0):
        """
        Initialize a square.

        Args:
            size (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare equality based on square area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Compare inequality based on square area."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Compare if this square is smaller than another based on area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Compare if this square is smaller or equal to another based on area."""
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        """Compare if this square is greater than another based on area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Compare if this square is greater or equal to another based on area."""
        return self.__gt__(other) or self.__eq__(other)
