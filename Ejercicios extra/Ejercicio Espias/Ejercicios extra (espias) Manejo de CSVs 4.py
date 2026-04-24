#     Cree un programa que abra un archivo .csv con la información de videojuegos 
# ( en base al CSV que fue generado en el ejercicio 1) y:

# Identifique los juegos de Clasificación "M":

    # Si el juego es "M", debes imprimir su nombre encriptado (sustituye todas las vocales por un asterisco *).

    # Ejemplo: GTA V -> GT* V | Elden Ring -> *ld*n R*ng.

    # Usa un prefijo: [CLASSIFIED] GT* V.

# Identifique los demás juegos:

    # Si no es "M", imprímelo normal con el prefijo: [PUBLIC] Minecraft.

# Conteo Final: Al terminar, muestra cuántos juegos "M" fueron protegidos.


import csv

def open_game_csv(games_csv):
    with open(games_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        classified_games = 0
        for row in reader:            
            if row["Clasificacion"] == "M":
                classified_games += 1
                nombre = row["Nombre"]
                for vocal in "aeiouAEIOU":
                    nombre = nombre.replace(vocal, "*")
                print(f'\n-[CLASSIFIED] {nombre}')
            else:
                print(f'\n-[PUBLIC] {row["Nombre"]}') 
    print(f"\nSe encontraron {classified_games} protegidos.")     # print(f"\nNo se encontraron juegos desarrollados por: {user_developer}.")

open_game_csv('games.csv')




