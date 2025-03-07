#!/usr/bin/python3
"""Module Square"""


class Square:
    """Square class defined by a geometric shape

    Attributes:
        size (int): Size of square
    """

    def __init__(self, size=0):
        """
        Initialize method

        Args:
            size (int): Value to assign to square size

        Raises:
            TypeError: If size is not int
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
