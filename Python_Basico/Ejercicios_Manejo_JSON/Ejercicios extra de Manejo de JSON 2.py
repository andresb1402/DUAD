# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:

# Pida al usuario un tipo de Pokémon
# Muestre todos los Pokémon que sean de ese tipo


import json

def json_file_reader(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        pokemon_list_py = json.load(file)
    return pokemon_list_py


def find_and_print_type(pokemon_list_py):
    user_type = input('Please enter the Type you want to search: ').capitalize()
    pokemon_counter = 0
    pokemon_found = []
    for pokemon in pokemon_list_py:
        name = pokemon['name']['english']
        type = ", ".join(pokemon['type'])

        if user_type in type:
            pokemon_counter += 1
            pokemon_found.append(name)
            
    if pokemon_counter == 0:
        print(f'\nNo results for {user_type} Type.')
    else:
        print(f"\n--- Pokémon of type: {user_type} ---")
        for pokemon in pokemon_found:
            print(f"-{pokemon}")

poke_list = json_file_reader('json_pokemon.json')
find_and_print_type(poke_list)
