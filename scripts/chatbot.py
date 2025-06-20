# chatbot.py (para ejecutar desde el Escritorio)
import numpy as np
from sentence_transformers import SentenceTransformer

# Cargar archivos (busca en el mismo directorio)
embeddings = np.load("embeddings.npy")
with open("segmentos.txt", "r", encoding="utf-8") as f:
    segmentos = f.read().split("\n\n===\n\n")

modelo = SentenceTransformer('all-MiniLM-L6-v2')

def buscar_respuesta(pregunta):
    pregunta_embed = modelo.encode([pregunta])
    similitudes = np.dot(embeddings, pregunta_embed.T).flatten()
    indice_mas_similar = np.argmax(similitudes)
    return segmentos[indice_mas_similar]

print("🤖 Chatbot activado (escribe 'salir' para terminar)")
while True:
    pregunta = input("\nTú: ")
    if pregunta.lower() == "salir":
        break
    print("\n🔎 Respuesta:", buscar_respuesta(pregunta)[:500])  # Muestra los primeros 500 caracteres