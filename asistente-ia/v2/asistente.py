import requests
from config import API_KEY, MODELO
from historial import guardar

# Constante en lugar de URL hardcodeada en medio del código
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def preguntar(mensaje, historial):
    historial.append({"role": "user", "content": mensaje})
    try:
        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODELO,
                "messages": historial
            }
        )
        # Verificamos que la respuesta HTTP sea exitosa antes de parsear
        response.raise_for_status()
        respuesta = response.json()["choices"][0]["message"]["content"]
        historial.append({"role": "assistant", "content": respuesta})
        guardar(historial)
        return respuesta
    except requests.exceptions.HTTPError as e:
        # Error HTTP específico — 404, 429, 500, etc.
        return f"❌ Error HTTP: {e}"
    except KeyError:
        # La API respondió pero sin el formato esperado
        return "❌ La IA no respondió correctamente, intenta de nuevo"
    except Exception as e:
        # Cualquier otro error inesperado
        return f"❌ Error inesperado: {e}"