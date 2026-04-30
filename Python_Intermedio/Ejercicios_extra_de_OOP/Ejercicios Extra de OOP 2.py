#     Cree una clase base Animal y dos clases hijas Dog y Cat:

# Animal debe tener nombre y método speak() que retorne "Hace un sonido"
# Dog debe sobrescribir speak() para decir "Guau"
# Cat debe sobrescribir speak() para decir "Miau"


class Animal:
    def __init__(self, age, name):
        self.name = name
        self.age = age


    def speak(self):
        return "Sound"


class Dog(Animal):
    def __init__(self, age, name='Dog'):
        super().__init__(age, name)


    def speak(self):
        return 'Guau'


class Cat(Animal):
    def __init__(self, age, name='Cat'):
        super().__init__(age, name)
    
    
    def speak(self):
        return 'Miau'


pets = [Dog(4, "Bobby"), Cat(2, "Chimuelo")]
print('\n--- My Pets ---')
for i, animal in enumerate(pets, start=1):
    print(f'\n{i}- Name:    {animal.name}')
    print(f'   Age:     {animal.age} years old')
    print(f'   Does:    {animal.speak()}')
    print('-' * 30)