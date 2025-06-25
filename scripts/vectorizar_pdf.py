import pdfplumber
from sentence_transformers import SentenceTransformer
import numpy as np
import os

# --- RUTA ACTUALIZADA ---
pdf_path = "data/info_11_01.pdf"  # ← asegúrate de que el archivo esté allí

# --- FUNCIÓN PARA EXTRAER TEXTO ---
def extraer_texto(pdf_path):
    print("🔍 Extrayendo texto del PDF con pdfplumber...")
    try:
        texto = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    texto += page_text + "\n"
        return texto
    except Exception as e:
        print(f"❌ Error al leer el PDF: {e}")
        return None

# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    if not os.path.exists(pdf_path):
        print(f"⚠️ Archivo no encontrado: {pdf_path}")
    else:
        texto = extraer_texto(pdf_path)
        if texto:
            print(f"✅ Texto extraído (primeros 500 caracteres):\n{texto[:500]}...\n")

            # Dividir en segmentos por saltos dobles de línea
            segmentos = [p.strip() for p in texto.split('\n\n') if p.strip()]
            print(f"📊 Número de segmentos creados: {len(segmentos)}")

            # Generar embeddings
            print("🔄 Generando embeddings...")
            modelo = SentenceTransformer('all-MiniLM-L6-v2')
            embeddings = modelo.encode(segmentos)

            # Guardar los archivos en carpeta scripts
            np.save("scripts/embeddings.npy", embeddings)
            with open("scripts/segmentos.txt", "w", encoding="utf-8") as f:
                for s in segmentos:
                    f.write(s.replace("\n", " ").strip() + "\n")

            print("🎉 ¡Proceso completado!")
