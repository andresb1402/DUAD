# Cree una clase Employee con los siguientes requisitos:

#     Atributos privados: _name, _salary
#     Use @property y @<atributo>.setter para:
#         Mostrar el nombre y el salario
#         Validar que el salario nunca sea negativo
#     Cree un método promote que aumente el salario un porcentaje definido


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            print("Error: Name cannot be empty.")
        else:
            self._name = value


    @property
    def salary(self):
        return self._salary


    @salary.setter
    def salary(self, value):
        if value <= 0:
            print("Error: Salary must be greater than 0")
        else:
            self._salary = value


    def promote(self, percentage):
        self.salary = self.salary * (1 + percentage)
        return self.salary
    


employee = Employee('Jose', 1000)
employee.name = '' # "Error: Name cannot be empty."
employee.salary = -500 # "Error: Salary must be greater than 0"

employee.promote(0.5)
print(f'\nThe new salary of {employee.name} is {employee.salary}')