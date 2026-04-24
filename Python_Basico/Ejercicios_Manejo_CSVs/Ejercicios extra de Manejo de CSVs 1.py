# Cree un programa que abra un archivo .csv con la información de 
# videojuegos (el que fue generado en el ejercicio 1) 
# y: Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea

import csv

def open_game_csv(games_csv):
    with open(games_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f'Juego: {row["Nombre"]}')
            print(f'Genero: {row["Genero"]}')
            print(f'Desarrollador: {row["Desarrollador"]}')
            print(f'Clasificacion: {row["Clasificacion"]}\n')


open_game_csv('games.csv')




