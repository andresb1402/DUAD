# 3. Cree un programa con un numero secreto del 1 al 10. 
# El programa no debe cerrarse hasta que el usuario adivine el numero.

import random

secret_number = random.randint(1,10)
while True:
    #secret_number = random.randint(1,10) #Opcion para hacerlo un poco mas dificil de adivinar. 
    user_number = int(input("Intente adivinar el numero (1-10): "))
    if user_number == secret_number:
        print(f"Felicidades, ha adivinado el numero secreto {user_number}")
        break
    else:
        print(f"Numero {user_number} incorrecto, vuelve a intentar...")

