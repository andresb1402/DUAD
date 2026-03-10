# Cree una calculadora por linea de comando. Esta debe de tener un número actual, 
# y un menú para decidir qué operación hacer con otro número:

# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado

# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. 
# El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, 
# o si ingresa un número invalido a la hora de hacer la operación.

# num1 = int(input("Please enter the first number: "))
# print(f"Your current number is {num1}.\n")
# num2 = int(input("Please enter the second number: "))
# print(f"Your second number is {num2}.\n")

def sum(current, num2):
    result = current + num2
    print (f"The result of {current} + {num2} is {result}.\n")
    current = result
    print (f"Your new current number is: {current}.\n")
    return current


def subtraction(current, num2):
    result = current - num2
    print (f"The result of {current} - {num2} is {result}.\n")
    current = result
    print (f"Your new current number is: {current}.\n")
    return current


def division(current, num2):
    try:
        result = current / num2
        print (f"The result of {current} / {num2} is {result}\n")
        current = result
        print (f"Your new current number is: {current}.\n")
    except ZeroDivisionError:
        print("Error: We cannot divide by zero. Current number remains unchanged.\n")
    return current


def multiplication(current, num2):
    result = current * num2
    print (f"The result of {current} * {num2} is {result}.\n")
    current = result
    print (f"Your new current number is: {current}.\n")
    return current

def second_number():
    while True:
        try:
            num2 = int(input("\nPlease enter the second number: "))
            print(f"Your second number is {num2}.\n")
            return num2
        except ValueError:
            print("Error: Invalid input. Please enter a number.\n")


def menu():
    print("-----Operations-----")
    print("1. Sum")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Clear numbers")
    print("6. Exit.\n")
    

while True:
    try:
        current = int(input("Please enter the first number: "))
        print(f"Your current number is {current}.\n")
        break
    except ValueError:
        print("Error: Invalid input. Please enter a number.\n")
    

while True:
    
    menu()
    try:
        choice = int(input("Please enter the number of the operation you want: "))
    except ValueError:
        print("Error: Invalid option. Please enter a number between 1 and 6.\n")
        continue
    if choice == 1:
        num2 = second_number()
        current = sum(current, num2)
    elif choice == 2:
        num2 = second_number()
        current = subtraction(current, num2)
    elif choice == 3:
        num2 = second_number()
        current = division(current, num2)
    elif choice == 4:
        num2 = second_number()
        current = multiplication(current, num2)
    elif choice == 5:
        print("Result cleared...\n")
        current = int(input("Please enter the first number: "))
        print(f"Your current number is now {current}.\n")
    elif choice == 6:
        print("\n---Good bye---\n")
        break
    else:
        print("\nInvalid option. Please enter a valid number.\n")

