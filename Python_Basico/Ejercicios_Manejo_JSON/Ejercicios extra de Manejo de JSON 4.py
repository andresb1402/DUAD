# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:

# Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
# Calcule y muestre el promedio de nivel para cada tipo:


import json

def json_file_reader(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        pokemon_list_py = json.load(file)
    return pokemon_list_py

def filter_and_print_type(pokemon_list_py):
    pokemon_types = {}
    for pokemon in pokemon_list_py:
        level = pokemon['level']
        for t in pokemon['type']:
            if t not in pokemon_types:
                pokemon_types[t] = [level]
            else:
                pokemon_types[t].append(level)
    for type, list_of_levels in pokemon_types.items():
        avr_level = round(sum(list_of_levels) / len(list_of_levels), 2)

        print(f"Type: {type} → Average level: {avr_level}.")


poke_list = json_file_reader('json_pokemon.json')
filter_and_print_type(poke_list)
