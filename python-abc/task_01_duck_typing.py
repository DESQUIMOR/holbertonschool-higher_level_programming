#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract base class for shapes.
    Any class that inherits from Shape must implement area and perimeter methods.
    """
    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        """
        pass
    
    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    Circle implementation of Shape.
    """
    def __init__(self, radius):
        """
        Initialize a Circle with the given radius.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle using πr².
        
        Returns:
            float: The area of the circle
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle using 2πr.
        
        Returns:
            float: The perimeter of the circle
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Rectangle implementation of Shape.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle with the given width and height.
        
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate the area of the rectangle using width × height.
        
        Returns:
            float: The area of the rectangle
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle using 2(width + height).
        
        Returns:
            float: The perimeter of the rectangle
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Print information about a shape, using duck typing.
    
    This function demonstrates duck typing by not checking the type of the object,
    but simply using its methods. As long as the object has area() and perimeter()
    methods, it will work with this function.
    
    Args:
        shape: Any object that has area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
