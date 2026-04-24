import requests

API_KEY = "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"
historial = [
    {
        "role": "system",
        "content": "Eres un tutor de programación experto. Explicas todo de forma simple, con ejemplos prácticos, y siempre animas al estudiante. Te llamas Kai."
    }
]

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