# Cree una clase de Circle con:

#     Un atributo de radius (radio).
#     Un método de get_area que retorne su área.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = 3.14*(self.radius ** 2)
        return area

user_radius = float(input("Please enter the radius of the circle (in cm): "))
my_circle = Circle(user_radius)
print(f'\nArea: {my_circle.get_area():.2f} cm²')
