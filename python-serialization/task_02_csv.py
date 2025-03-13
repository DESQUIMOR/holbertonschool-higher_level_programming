import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file named data.json.
    Returns True if successful, otherwise returns False.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
