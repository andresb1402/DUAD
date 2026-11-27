# Stores the data

import json
from datetime import datetime
import shutil
from pathlib import Path

class CorruptedFileError(Exception):
    pass


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
    

def save_to_file(output_file, transactions_list):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(transactions_list, file, indent=4)


def backup_corrupted_file(input_file):
    current_date = datetime.now()
    date_txt = current_date.strftime("%Y-%m-%d_%H%M%S")
    original_path = Path(input_file)
    backup_name = f'{original_path.stem}_{date_txt}{original_path.suffix}'
    backup_path = original_path.with_name(backup_name)
    shutil.move(input_file, backup_path)
    
    return backup_path


def save_rejected_transactions(original_file, rejected_transactions):
    current_date = datetime.now()
    date_txt = current_date.strftime("%Y-%m-%d_%H%M%S")
    original_path = Path(original_file)
    rejected_name = f'{original_path.stem}_rejected_{date_txt}{original_path.suffix}'
    rejected_path = original_path.with_name(rejected_name)
    save_to_file(rejected_path, rejected_transactions)
    
    return rejected_path
