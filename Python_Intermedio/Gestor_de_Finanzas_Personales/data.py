# Stores the data

import json

def json_file_reader(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise CorruptedFileError("The transactions file is corrupted.")
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        raise CorruptedFileError("The transactions file is corrupted.") from e
    


def save_to_file(input_file, transactions_list):
    with open(input_file, 'w', encoding='utf-8') as file:
        json.dump(transactions_list, file, indent=4)

class CorruptedFileError(Exception):
    pass