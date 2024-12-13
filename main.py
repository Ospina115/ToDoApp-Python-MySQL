# Archivo principal de la aplicación
import json
import mysql.connector
from ui import create_ui

def export_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def import_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    create_ui()