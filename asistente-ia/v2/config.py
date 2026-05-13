import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODELO = os.getenv("MODELO", "nvidia/nemotron-3-super-120b-a12b:free")
SYSTEM_PROMPT = "Eres un tutor de programación experto. Explicas todo de forma simple, con ejemplos prácticos, y siempre animas al estudiante. Te llamas Kai."