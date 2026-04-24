# 1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

# Si le salen errores, no se asuste. 
# Lealos e intente comprender qué significan.
# Los errores son oportunidades de aprendizaje.

name = "Jose"
age = 32
fav_number = 14
lucky_numbers = [14,24,45,80]
unlucky_numbers = [10,20,33]

#print("Mi edad es " + age) # TypeError: can only concatenate str (not "int") to str
print("Mi nombre es " + name)
print(f"Mi nombre es {name}")
#print(fav_number + "es mi numero favorito") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("Mi edad es", age)
print(f"Mi edad es {age}")
print(fav_number, "es mi numero favorito")
print(lucky_numbers + unlucky_numbers)
#print("My lucky numbers are " + lucky_numbers) #TypeError: can only concatenate str (not "list") to str
print("My lucky numbers are", lucky_numbers)
print(3.14 + 5)
print(True + False)


