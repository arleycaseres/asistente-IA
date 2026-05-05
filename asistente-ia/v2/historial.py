import json
import os
from config import SYSTEM_PROMPT

ARCHIVO = "historial.json"

def cargar():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return [{"role": "system", "content": SYSTEM_PROMPT}]

def guardar(historial):
    with open(ARCHIVO, "w") as f:
        json.dump(historial, f, indent=2)