#!/usr/bin/python3
"""
Example Google style docstrings.
"""


class Square:
    """
    Square class representing a geometric shape.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize the Square class.

        Args:
            size (int): The size of the square, must be a non-negative integer.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

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
