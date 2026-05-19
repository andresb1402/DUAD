# Cree una clase base Vehicle con los atributos:

#     _brand
#     _year

# Agregue un método get_info() que devuelva una descripción del vehículo.

# Luego cree dos clases hijas:

#     Car
#     Motorcycle

# Cada una debe agregar su propio atributo (por ejemplo, doors o type) 
# y sobrescribir el método get_info() para incluir esta información adicional.


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


    def get_info(self):
        return f"Brand: {self.brand}, Year: {self.year}"


class Bike(Vehicle):
    def __init__(self, brand, year, bike_type):
        super().__init__(brand, year)
        self.bike_type = bike_type

    def get_info(self):
        return f"{super().get_info()}, Type: {self.bike_type}"



class Car(Vehicle):
    def __init__(self, _brand, _year, doors):
        super().__init__(_brand, _year)
        self.doors = doors

    def get_info(self):
        return f"{super().get_info()}, Doors: {self.doors}"
    

vehicle1 = Car("Toyota", 1998, 4)
vehicle2 = Bike("Husqvarna", 2014, "Enduro")


print(vehicle1.get_info())
print(vehicle2.get_info())