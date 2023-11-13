"""Create a class Point that represents a coordinate!"""

from __future__ import annotations


class Point:
    """A point on a 2D plane!"""
    x: float
    y: float

    def __init__(self, x_input: float = 0.0, y_input: float = 0.0):
        """Construct a point by giving x and y coordinates!"""
        self.x = x_input
        self.y = y_input

    def scale_by(self, factor: int) -> None:
        """Scale the point by a factor!"""
        self.x: float = self.x * factor
        self.y: float = self.y * factor
  
    def scale(self, factor: int) -> Point:
        """Return a new point scaled by a factor!"""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
       
    def __str__(self) -> str:
        """Return a string representation of the point!"""
        return f"x: {self.x}; y: {self.y}"
      
    def __mul__(self, factor: int | float) -> Point:
        """Create a new point scaled by a factor from exising point!"""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, factor: int | float) -> Point: 
        """Create a new point added by a factor from exising point!"""
        return Point(self.x + factor, self.y + factor)