import json
import os
from config import SYSTEM_PROMPT

ARCHIVO = "historial.json"

def cargar():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:  # encoding explícito
            return json.load(f)
    return [{"role": "system", "content": SYSTEM_PROMPT}]

def guardar(historial):
    with open(ARCHIVO, "w", encoding="utf-8") as f:  # encoding explícito
        json.dump(historial, f, indent=2, ensure_ascii=False)  # ensure_ascii=False para tildes y ñ