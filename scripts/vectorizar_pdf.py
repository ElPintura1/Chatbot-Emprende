from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np
import os

# --- CONFIGURACIÓN ---
pdf_path = "C:/Users/Chocl/Desktop/info_11_01.pdf"  # Asegúrate de que esta ruta sea correcta

# --- FUNCIÓN PARA EXTRAER TEXTO ---
def extraer_texto(pdf_path):
    print("🔍 Extrayendo texto del PDF...")
    try:
        reader = PdfReader(pdf_path)
        texto = ""
        for page in reader.pages:
            texto += page.extract_text() + "\n"
        return texto
    except Exception as e:
        print(f"❌ Error al leer el PDF: {e}")
        return None

# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    # Verificar si el PDF existe
    if not os.path.exists(pdf_path):
        print(f"⚠️ Archivo no encontrado: {pdf_path}")
    else:
        # 1. Extraer texto
        texto = extraer_texto(pdf_path)
        if texto:
            print(f"✅ Texto extraído (primeros 300 caracteres):\n{texto[:300]}...")
            
            # 2. Dividir en segmentos
            segmentos = [p.strip() for p in texto.split('\n\n') if p.strip()]
            print(f"\n📊 Número de segmentos: {len(segmentos)}")
            
            # 3. Generar embeddings
            print("\n🔄 Generando embeddings... (esto puede tomar unos minutos)")
            modelo = SentenceTransformer('all-MiniLM-L6-v2')
            embeddings = modelo.encode(segmentos)
            
            # 4. Guardar resultados
            np.save("embeddings.npy", embeddings)
            with open("segmentos.txt", "w", encoding="utf-8") as f:
                f.write("\n\n===\n\n".join(segmentos))
            
            print("\n🎉 ¡Proceso completado! Archivos generados:")
            print(f"- embeddings.npy (vectores numéricos, tamaño: {embeddings.shape})")
            print(f"- segmentos.txt (texto procesado)")
