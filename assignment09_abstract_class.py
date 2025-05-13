from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(Self):
        pass

class Rectangele(Shape):
    def __init__(Self, length, width):
        Self.length = length
        Self.width = width

    def area(Self):
        return Self.length * Self.width
    
rec = Rectangele(5, 10)
print(f"Area of the rectangle: {rec.area()}")