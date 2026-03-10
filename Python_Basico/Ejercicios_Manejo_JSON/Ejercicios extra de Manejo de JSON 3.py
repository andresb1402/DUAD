# Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:

# Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)


import json

def json_file_reader(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        pokemon_list_py = json.load(file)
    return pokemon_list_py


def print_list(pokemon_list_py):
    for pokemon in pokemon_list_py:
        name = pokemon['name']['english']
        attack = pokemon['base']['Attack']
        defense = pokemon['base']['Defense']
        speed = pokemon['base']['Speed']

        print(f"Name: {name}.")
        print(f"Attack: {attack}.")
        print(f"Defense: {defense}.")
        print(f"Speed: {speed}.")
        print()


poke_list = json_file_reader('json_pokemon.json')
print_list(poke_list)
