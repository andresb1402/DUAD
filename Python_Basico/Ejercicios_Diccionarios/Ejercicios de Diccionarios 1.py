#Cree un diccionario que guarde la siguiente información sobre un hotel:

    # nombre
    # numero_de_estrellas
    # habitaciones

# El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:

#     numero
#     piso
#     precio_por_noche



single_room = {
    "Numero": 1,
    "Piso": 1,
    "Precio por noche": 20000,
}

double_room = {
    "Numero": 10,
    "Piso": 2,
    "Precio por noche": 30000,
}

rooms = [single_room, double_room]

hotel_5stars = {
    "Nombre": "Hotel 5 Stars",
    "Numero de estrellas": 5,
    "Habitaciones": rooms,
}

print(f'---Bienvenidos a {hotel_5stars["Nombre"]}---')
print(f'Su habitación será la #{rooms[0]["Numero"]}')
print(f'La podrá encontrar en el piso #{rooms[0]["Piso"]}') 
print(f'El precio por noche es de: {rooms[0]["Precio por noche"]}')

# print(f'Su habitación será la #{rooms[1]["Numero"]}')
# print(f'La podrá encontrar en el piso #{rooms[1]["Piso"]}') 
# print(f'El precio por noche es de: {rooms[1]["Precio por noche"]}')