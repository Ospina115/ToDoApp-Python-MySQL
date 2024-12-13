# Módulo para funciones utilitarias (por ejemplo, importar/exportar JSON)

import json

def export_to_json(tasks, filename):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def import_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)