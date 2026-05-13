from historial import cargar
from asistente import preguntar
import os
os.system('cls' if os.name == 'nt' else 'clear')
def menu():
    historial = cargar()
    print("🤖 Kai - escribe 'salir' para terminar")
    while True:
        pregunta = input("\nTú: ").strip()  # strip() elimina espacios accidentales
        if not pregunta:  # si el usuario presiona Enter sin escribir nada
            continue
        if pregunta.lower() == "salir":
            break
        respuesta = preguntar(pregunta, historial)
        print(f"\nKai: {respuesta}")

# Buena práctica — solo ejecuta menu() si corres este archivo directamente
if __name__ == "__main__":
    menu()