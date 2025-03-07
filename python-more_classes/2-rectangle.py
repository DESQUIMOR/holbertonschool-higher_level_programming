#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
    Rectangle Class

    Attributes:
        width (int): Private
        height (int): Private
    """

    def __init__(self, width=0, height=0):
        """
        Init Rectangle Class

        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width getter

        Returns:
            int: The width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter

        Args:
            value (int): A value to set
        
        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height getter

        Returns:
            int: The height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter

        Args:
            value (int): Value to be set
        
        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return Rectangle Area

        Returns:
            int: Rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of rectangle

        Returns:
            int: Rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
