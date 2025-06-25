# 🤖 Chatbot Personalizado Basado en Documentos

Este proyecto permite ejecutar un chatbot local que responde preguntas basadas exclusivamente en el contenido de un PDF cargado previamente. Utiliza inteligencia artificial ejecutada de forma local con Ollama y embeddings semánticos.

---

## 1. 🧩 Herramientas utilizadas

- [Ollama](https://ollama.com/) para ejecutar el modelo LLM localmente.
- `sentence-transformers` (modelo: `all-MiniLM-L6-v2`) para generar embeddings.
- `scikit-learn` para cálculo de similitud coseno.
- `PyPDF2` para lectura de PDFs.
- Editor de código: Cursor.
- Modelo LLM: `phi` (puede ser reemplazado por `mistral`, `llama2`, etc.).

---

## 2. 📂 Estructura del proyecto

```
AgenteConversacional/
│
├── data/
│   └── info_11_01.pdf         # PDF base de conocimiento
│
├── scripts/
│   ├── chatbot.py             # Script principal del asistente conversacional
│   └── vectorizar_pdf.py      # Código que transforma el PDF en embeddings
│
├── embeddings.npy             # Embeddings generados desde el PDF
├── segmentos.txt              # Fragmentos textuales del PDF
├── README.md                  # Este archivo
```

---

## 3. ▶️ Cómo correr el sistema

### 3.1 Clona o navega al proyecto
```bash
cd C:/Users/TU_USUARIO/Desktop/AgenteConversacional
```

### 3.2 (Opcional) Crea un entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3.3 Instala las dependencias necesarias
```bash
pip install sentence-transformers scikit-learn PyPDF2
```

### 3.4 Ejecuta el modelo LLM local
```bash
ollama run phi
```
> Mantén esta terminal abierta mientras usas el chatbot.

### 3.5 Vectoriza el contenido del PDF
```bash
python scripts/vectorizar_pdf.py
```

### 3.6 Ejecuta el chatbot en otra terminal
```bash
python scripts/chatbot.py
```

### 3.7 Finaliza escribiendo:
```
salir
```

---

## 4. 📌 Lógica del sistema

- El PDF se convierte en fragmentos textuales.
- Cada fragmento es vectorizado (embedding semántico).
- Al hacer una pregunta, se calcula la similitud con cada fragmento.
- Se seleccionan los 3 más relevantes y se construye un prompt.
- El prompt es enviado al modelo LLM que responde según el contenido.

---

## 5. 🎓 Aprendizajes

- Construcción de un chatbot local sin depender de APIs externas.
- Uso de embeddings con `sentence-transformers`.
- Extracción de texto desde PDFs.
- Manejo de codificación de caracteres (`UTF-8`, `latin1`).
- Integración de Ollama como backend para modelos ligeros.

---

## 6. 🧪 Preguntas usadas para probar el sistema
¿Cuál es el rol del educador dentro del proceso de formación emprendedora?

¿Qué competencias se consideran esenciales para desarrollar una mentalidad emprendedora?

¿Cuál es el objetivo principal de la educación emprendedora?


---

## 7. 📸 Evidencia de funcionamiento (imagen en repositorio)

El chatbot fue probado exitosamente, respondiendo de manera coherente y relevante con base únicamente en el contenido del PDF. Se corrigieron errores de codificación y se validaron las respuestas frente al contenido original.

---

## 8. ⚠️ Dificultades encontradas y soluciones

| Problema                                              | Solución                                                    |
|-------------------------------------------------------|-------------------------------------------------------------|
| 1. El modelo `phi` inventaba contenido                 | Se reemplazó temporalmente por `mistral`                    |
| 2. Caracteres extraños como Ã³, Ã¡                     | Se aplicó `.encode('latin1').decode('utf-8')`               |
| 3. El PDF inicial no era legible                      | Se reemplazó por una versión con OCR legible               |
| 4. Error en `chatbot.py` por dependencias             | Se corrigió la indentación y se instalaron los paquetes     |

---

## 9. 🚀 Comandos de Git usados para subir a GitHub

```bash
git init
git remote add origin https://github.com/ElPintura1/Manual-de-emprendedorismo.git
git add .
git commit -m "Proyecto chatbot educativo final"
git pull origin master --allow-unrelated-histories
git push -u origin master
```

---

¡Proyecto finalizado y funcional! 💻📚
