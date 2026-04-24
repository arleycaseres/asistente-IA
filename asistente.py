import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

def cargar_historial():
    if os.path.exists("historial.json"):
        with open("historial.json", "r") as f:
            return json.load(f)
    return [{"role": "system", "content": "Eres un tutor de programación experto. Explicas todo de forma simple, con ejemplos prácticos, y siempre animas al estudiante. Te llamas Kai."}]

def guardar_historial():
    with open("historial.json", "w") as f:
        json.dump(historial, f, indent=2)

historial = cargar_historial()

def preguntar(mensaje):
    historial.append({"role": "user", "content": mensaje})
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "inclusionai/ling-2.6-1t:free",
            "messages": historial
        }
    )
    
    respuesta = response.json()["choices"][0]["message"]["content"]
    historial.append({"role": "assistant", "content": respuesta})
    guardar_historial()  # ← esto faltaba
    return respuesta

def menu():
    print("🤖 Asistente IA con memoria - escribe 'salir' para terminar")
    while True:
        pregunta = input("\nTú: ")
        if pregunta.lower() == "salir":
            break
        respuesta = preguntar(pregunta)
        print(f"\nIA: {respuesta}")

menu()
