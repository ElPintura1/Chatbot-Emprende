import subprocess
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

modelo_ollama = "mistral"

def consultar_ollama(prompt):
    comando = ["ollama", "run", modelo_ollama, prompt]
    resultado = subprocess.run(comando, stdout=subprocess.PIPE, text=True)
    return resultado.stdout.strip()

modelo_embedding = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = np.load("scripts/embeddings.npy")

with open("scripts/segmentos.txt", "r", encoding="utf-8") as f:
    segmentos = f.readlines()

def encontrar_segmentos_relevantes(pregunta, top_n=3):
    emb_pregunta = modelo_embedding.encode([pregunta])
    similitudes = cosine_similarity(emb_pregunta, embeddings)
    idxs_mejores = np.argsort(similitudes[0])[::-1][:top_n]
    return "\n\n".join([segmentos[i] for i in idxs_mejores])

print("🤖 Chatbot activado (escribe 'salir' para terminar)")

while True:
    entrada = input("Tú: ")
    if entrada.lower() == "salir":
        break

    contexto = encontrar_segmentos_relevantes(entrada)

    prompt = f"""
Eres un asistente experto en educación emprendedora.

Solo puedes usar como fuente de información el texto que te entrego a continuación.
Si no encuentras la respuesta exactamente en ese texto, responde:
"No encontré información suficiente en el documento para responder eso".

--- TEXTO DEL MANUAL ---
{contexto}

--- PREGUNTA ---
{entrada}

--- RESPUESTA ---
"""

    respuesta = consultar_ollama(prompt)
    print("Bot:", respuesta.encode('latin1').decode('utf-8', errors='ignore'))
