#Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.

suma = 0
numeros = []
for i in range(100):
    numero = int(input("Por favor ingrese un numero: "))
    numeros.append(numero)
    suma += numero
operacion = " + ".join(str(n) for n in numeros)
print(f"{operacion} = {suma}")
