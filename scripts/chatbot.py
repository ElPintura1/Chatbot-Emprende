import subprocess
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Función para consultar al modelo (ajustado para PHI u otro compatible)
def consultar_ollama(prompt):
    comando = ['ollama', 'run', 'phi', prompt]  # Puedes cambiar 'phi' por 'mistral', 'llama2', etc.
    resultado = subprocess.run(comando, stdout=subprocess.PIPE, text=True)
    return resultado.stdout.strip()

# Cargar modelo de embeddings
modelo_embedding = SentenceTransformer("all-MiniLM-L6-v2")

# Cargar embeddings y segmentos
embeddings = np.load("embeddings.npy")
with open("segmentos.txt", "r", encoding="utf-8") as f:
    segmentos = f.readlines()

# Buscar los 3 segmentos más relevantes
def encontrar_segmentos_relevantes(pregunta, top_n=3):
    emb_pregunta = modelo_embedding.encode([pregunta])
    similitudes = cosine_similarity(emb_pregunta, embeddings)
    idxs_mejores = np.argsort(similitudes[0])[::-1][:top_n]
    return "\n\n".join([segmentos[i] for i in idxs_mejores])

# Loop principal del chatbot
print("🤖 Chatbot activado (escribe 'salir' para terminar)")

while True:
    entrada = input("Tú: ")
    if entrada.lower() == "salir":
        break

    contexto = encontrar_segmentos_relevantes(entrada)

    prompt = f"""Eres un asistente experto en educación emprendedora.
Tu única fuente de información debe ser el texto proporcionado a continuación. 
No debes inventar nada. Si no encuentras la respuesta en el texto, di: "No encontré información suficiente en el documento para responder eso".

--- TEXTO DEL MANUAL ---
{contexto}

--- PREGUNTA ---
{entrada}

--- RESPUESTA ---"""

    respuesta = consultar_ollama(prompt)
    print("Bot:", respuesta)
