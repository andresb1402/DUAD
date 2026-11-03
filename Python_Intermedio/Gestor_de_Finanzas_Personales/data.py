# Stores the data

import json

def json_file_reader(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    

def save_to_file(input_file, transactions_list):
    with open(input_file, 'w', encoding='utf-8') as file:
        json.dump(transactions_list, file, indent=4)
