from abc import ABC, abstractmethod
import math

# Základní třída Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def __int__(self):
        # Vrací oblast jako celé číslo
        return int(self.area())
    
    def __str__(self):
        # Vrací informace o tvaru
        return f'{self.__class__.__name__} with area: {self.area()}'

# Třída Rectangle (Obdélník)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Třída Circle (Kružnice)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

# Třída RightTriangle (Pravoúhlý trojúhelník)
class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Třída Trapezoid (Lichoběžník)
class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

# Ukázka použití
shapes = [
    Rectangle(5, 10),
    Circle(7),
    RightTriangle(3, 4),
    Trapezoid(3, 4, 5)
]

for shape in shapes:
    print(f'{shape} (as integer area): {int(shape)}')
