from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Method to calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate the perimeter of the shape"""
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

def shape_info(shape: Shape):
    """Function to print area and perimeter of a shape using duck typing"""
    if not isinstance(shape, Shape):
        raise TypeError("Expected an instance of Shape")
    print(f"Area: {shape.area():.5f}")
    print(f"Perimeter: {shape.perimeter():.5f}")
