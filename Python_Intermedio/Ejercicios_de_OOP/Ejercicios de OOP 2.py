# Cree una clase de Bus con:

#     Un atributo de max_passengers.
#     Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). 
#       Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
#     Un método para bajar pasajeros uno por uno (en cualquier orden).

class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []


    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"\n--- Passenger {person.name} has entered the bus. ---")
        else:
            print(f'\nPassenger {person.name} could not enter, the bus is full.')


    def remove_passenger(self):
        if len(self.passengers) > 0:
            leaving_person = self.passengers.pop()
            print(f"\n--- {leaving_person.name} has left the bus. ---")
        else:
            print("\nThe bus is already empty! Nobody to remove.")

    
    def show_passengers(self):
        if len(self.passengers) > 0:
            print(f"\n--- Passengers on board ---")
            for i, p in enumerate(self.passengers, start=1):
                print(f'{i}. {p.name}')
        else:
            print("\nThe bus is empty! Nobody to show.")

while True:
    try:
        max_passengers = int(input("\nPlease enter the max passengers: "))
        break
    except ValueError:
        print('\nError: Please enter a numeric value.')

my_bus = Bus(max_passengers)

while True:
    print('\n1. Add a passenger.')
    print('2. Remove a passenger.')
    print('3. Show passengers.')
    print('4. Exit.')

    try:
        choice = int(input('\nEnter your option (1-4): '))
        
        if choice == 1:
            while True:
                name = input("\nEnter the name of the passenger: ")
                if name.isspace() or len(name) == 0 or name.isdigit():
                    print("Error: Name cannot be empty, a space or a number.")
                    continue
                new_passenger = Person(name)
                my_bus.add_passenger(new_passenger)
                break

        elif choice == 2:
            my_bus.remove_passenger()
            

        elif choice == 3:
            my_bus.show_passengers()
            
        
        elif choice == 4:
            print('\nGood bye.')
            break

        else:
            print('\nPlease enter a valid option (1-4).')

    except ValueError:
        print('\nPlease enter a numeric value (1-4)')

