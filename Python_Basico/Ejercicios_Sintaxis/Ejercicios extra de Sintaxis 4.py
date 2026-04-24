#Tabla de multiplicar personalizada

    # Pida al usuario un número del 1 al 10
    # Muestre su tabla de multiplicar del 1 al 12


while True:
    number = int(input("Ingrese un número (1-10): "))
    if number > 10:
        print("El numero debe ser entre 1 y 10. Intente de nuevo.")
    elif number <= 10:
        for i in range(0, 12):
            print(f"{number} x {i+1} = {number*(i+1)}")
        break
