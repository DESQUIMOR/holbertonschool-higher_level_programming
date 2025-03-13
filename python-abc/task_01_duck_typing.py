#!/usr/bin/env python3
"""
Module implementing abstract shape classes and duck typing example.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Method to calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class implementing the Shape interface."""

    def __init__(self, radius: float):
        """Initialize circle with given radius.

        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle
        """
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class implementing the Shape interface."""

    def __init__(self, width: float, height: float):
        """Initialize rectangle with given width and height.

        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape: Shape):
    """Function to print area and perimeter of a shape using duck typing.

    Args:
        shape (Shape): Any object implementing the Shape interface
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
