#     Cree un programa que abra un archivo .csv con la información de videojuegos 
# ( en base al CSV que fue generado en el ejercicio 1) y:

# Lea el archivo .csv con videojuegos
# Cuente cuántos videojuegos hay de cada género
# Muestre el resultado de forma ordenada

import csv

def game_csv_counter(games_csv):
    with open(games_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print("Generos encontrados: \n")
        counter = {}
        for row in reader:   
            current_genre = row["Genero"]         
            if current_genre in counter:
                counter[current_genre] += 1
            else:
                counter[current_genre] = 1
        sorted_list = sorted(counter.items())
    for genre, amount in sorted_list:
        print(f"{genre}: {amount}")
    return counter
    

game_csv_counter('games.csv')






