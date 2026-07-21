# Stores the data

import json

def json_file_reader(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    

def save_to_file(input_file, clients_list):
    with open(input_file, 'w') as file:
        json.dump(clients_list, file, indent=4)
