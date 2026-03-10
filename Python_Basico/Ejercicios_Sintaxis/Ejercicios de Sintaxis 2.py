# 2. Cree un programa que le pida al usuario su nombre, apellido, y edad, 
# y muestre si es un bebé, niño, preadolescente, adolescente, 
# adulto joven, adulto, o adulto mayor.

name = (input("Ingrese su nombre: "))
lastname = (input("Ingrese su apellido: "))
age = int(input("Ingrese su edad: "))

if age <= 2:
    label = "es un bebé"
elif age <= 10:
    label = "es un niñ@"
elif age <= 12:
    label = "es un preadolescente" 
elif age <= 17:
    label = "es un adolescente"
elif age <= 25:
    label = "es un adulto joven"
elif age <= 59:
    label = "es un adulto"
else:
    label = "es un adulto mayor"

print(f"{name} {lastname} de {age} años {label}")  

