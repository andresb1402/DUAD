# Cree una clase abstracta de Shape que:

#     Tenga los métodos abstractos de calculate_perimeter y calculate_area.
#     Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
#     Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def __str__(self):
        return f"Circle with radius {self.radius}"
    

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)
    

class Square(Shape):
    def __init__(self, side):
        self.side = side

    
    def __str__(self):
        return f"Square with side {self.side}"
    

    def calculate_perimeter(self):
        return 4 * self.side
    

    def calculate_area(self):
        return self.side ** 2
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"
    

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    

    def calculate_area(self):
        return self.width * self.height
    

circle = Circle(5)
square = Square(4)
rectangle = Rectangle(5, 8)

shapes = [circle, square, rectangle]
for s in shapes:
    perimeter = s.calculate_perimeter()
    area = s.calculate_area()
    print(f"The perimeter of the {s} is {perimeter:.2f}cm.")
    print(f"The area of the {s} is {area:.2f}cm².\n")

