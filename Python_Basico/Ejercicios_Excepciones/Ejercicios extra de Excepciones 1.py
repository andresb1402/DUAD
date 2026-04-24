#Pida al usuario su nombre

# Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")

#Luego pida su edad

# Si no es un número válido, capture el ValueError y muestre un mensaje

#Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"

def name_function():
    while True:  
        try:
            name = input("Por favor ingrese su nombre: ")
            if name.isdigit():
                raise ValueError("El nombre no puede ser un número.")
            break
        except ValueError as e:
            print(e)
    return name

def age_function():
    while True:
        try:
            age = int(input("Por favor ingrese su edad: "))
            break
        except ValueError:
            print("La edad debe ser un número válido.")
    return age

print(f"Hola {name_function()}, su edad es {age_function()}.") 