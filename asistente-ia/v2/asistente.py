import requests
from config import API_KEY, MODELO
from historial import guardar

def preguntar(mensaje, historial):
    historial.append({"role": "user", "content": mensaje})
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODELO,
                "messages": historial
            }
        )
        respuesta = response.json()["choices"][0]["message"]["content"]
        historial.append({"role": "assistant", "content": respuesta})
        guardar(historial)
        return respuesta
    except Exception as e:
        return f"❌ Error: {e}"