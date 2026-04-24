#Cree un algoritmo que le pida 2 números al usuario, 
#los guarde en dos variables distintas (primero y segundo) 
#y los ordene de menor a mayor en dichas variables.

#Ejemplos:

#A: 56, B: 32 → A: 32, B: 56
#A: 24, B: 76 → A: 24, B: 76
#A: 45, B: 12 → A: 12, B: 45

primero = int(input("Por favor ingrese el primer numero: "))
print()
segundo = int(input("Por favor ingrese el segundo numero: "))
print()
if primero > segundo:
    print(f"A: {primero}, B: {segundo} → A: {segundo}, B: {primero}")
elif segundo > primero:
    print(f"A: {primero}, B: {segundo} → A: {primero}, B: {segundo}")
else: 
    print(f"A: {primero}, B: {segundo} → A: {segundo}, B: {primero}")


    

