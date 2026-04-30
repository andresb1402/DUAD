#     Cree una clase Rectangle que:

# Tenga atributos width y height
# Tenga un método get_area() que retorne el área
# Tenga un método get_perimeter() que retorne el perímetro
# Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
    

    def get_area(self):
        area = self.width * self.height
        return area
    

    def is_square(self):
        return self.width == self.height

while True:
    try:
        width = float(input("\nPlease enter the width (in cm): "))
        if width <= 0:
            print(f"\nError. Width must be greater than zero.")
            continue
        height = float(input("Please enter the height (in cm): "))
        if height <= 0:
            print(f"\nError. Height must be greater than zero.")
            continue
        shape = Rectangle(width, height)
        break
    except ValueError:
        print("\nError: Value must be a number.")

print('\n--- Results ---')
print(f'\nPerimeter: {shape.get_perimeter():.2f} cm')
print(f'Area: {shape.get_area():.2f} cm²')
print(f'Is this a square? {shape.is_square()}\n')

