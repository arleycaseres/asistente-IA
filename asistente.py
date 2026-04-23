import requests

API_KEY = "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"

def preguntar(mensaje):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "inclusionai/ling-2.6-1t:free",
            "messages": [
                {"role": "user", "content": mensaje}
            ]
        }
    )
    data = response.json()
    if "choices" not in data:
        print(f"Error: {data}")
        return "Error en la respuesta"
    return data["choices"][0]["message"]["content"]

def menu():
    print("🤖 Asistente IA - escribe 'salir' para terminar")
    while True:
        pregunta = input("\nTú: ")
        if pregunta.lower() == "salir":
            break
        respuesta = preguntar(pregunta)
        print(f"\nIA: {respuesta}")

menu()