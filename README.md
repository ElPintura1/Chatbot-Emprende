# Chatbot-Emprende 🤖

Este proyecto consiste en la construcción de un chatbot local que responde exclusivamente con base en el contenido de documentos PDF previamente vectorizados. Es una solución educativa, gratuita y sin necesidad de conexión a la nube.

## 🚀 Funcionalidades principales

- Conversación con un agente local sin internet.
- Respuestas basadas únicamente en el contenido de un PDF vectorizado.
- Implementación con modelo de lenguaje local usando [Ollama](https://ollama.com).
- Integración de embeddings con `sentence-transformers`.

## 🧠 Tecnologías usadas

- Python 3.10+
- Ollama (con modelos como `phi`, `mistral`, o `tinyllama`)
- Sentence Transformers (`all-MiniLM-L6-v2`)
- GitHub / GitHub Desktop
- Editor de código Cursor

## 🗂 Estructura del proyecto


## 📝 Instrucciones de uso

1. Instalar los requisitos (`pip install -r requirements.txt`)
2. Ejecutar `vectorizar_pdf.py` para procesar el PDF
3. Ejecutar `chatbot.py` para conversar con el agente
4. Hacer preguntas relacionadas con el contenido del documento

## ✅ Estado del proyecto

> ✔️ Vectorización funcionando  
> ✔️ Chatbot operativo con modelo `phi`  
> ⏳ En desarrollo mejoras de contexto múltiple y multilingüe

## 📄 Licencia

Este proyecto es de uso académico y personal. Puedes adaptarlo libremente para fines educativos.
