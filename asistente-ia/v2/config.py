import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODELO = "inclusionai/ling-2.6-1t:free"
SYSTEM_PROMPT = "Eres un tutor de programación experto. Explicas todo de forma simple, con ejemplos prácticos, y siempre animas al estudiante. Te llamas Kai."