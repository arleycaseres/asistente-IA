from historial import cargar
from asistente import preguntar

def menu():
    historial = cargar()
    print("🤖 Kai - escribe 'salir' para terminar")
    while True:
        pregunta = input("\nTú: ")
        if pregunta.lower() == "salir":
            break
        respuesta = preguntar(pregunta, historial)
        print(f"\nKai: {respuesta}")

menu()