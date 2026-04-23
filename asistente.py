import requests

API_KEY = "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"
historial = []

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