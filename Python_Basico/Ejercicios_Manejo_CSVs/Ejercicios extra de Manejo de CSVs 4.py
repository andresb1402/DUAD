#     Cree un programa que abra un archivo .csv con la información de videojuegos 
# ( en base al CSV que fue generado en el ejercicio 1) y:

# Lea el archivo .csv con videojuegos
# Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
# Muestre todos los videojuegos desarrollados por esa empresa en formato legible:

import csv

def open_game_csv(games_csv):
    with open(games_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        user_developer = input("Por favor ingrese el desarrollador: ").strip().capitalize()
        found_games = False
        for row in reader:            
            if user_developer == row["Desarrollador"]:
                print(f'\n-{row["Nombre"]} (Clasificacion: {row["Clasificacion"]}, Genero: {row["Genero"]})')
                found_games = True
        if found_games == False:
            print(f"\nNo se encontraron juegos desarrollados por: {user_developer}.")

open_game_csv('games.csv')




