#     Cree un programa que abra un archivo .csv con la información de videojuegos 
# ( en base al CSV que fue generado en el ejercicio 1) y:

# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
# Muestre todos los videojuegos que tengan esa clasificación

import csv

def open_game_csv(games_csv):
    with open(games_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        user_classification = input("Please enter the classification: ").strip().upper()
        found_games = False
        for row in reader:            
            if user_classification == row["Clasificacion"]:
                print(f'\nJuego: {row["Nombre"]}')
                print(f'Genero: {row["Genero"]}')
                print(f'Desarrollador: {row["Desarrollador"]}')
                print(f'Clasificacion: {row["Clasificacion"]}\n')
                found_games = True
        if found_games == False:
            print(f"No games found with the classification {user_classification}.")

open_game_csv('games.csv')




