from fastapi import FastAPI
from pydantic import BaseModel
from knowledge_base import SmartKnowledgeBase
from fastapi.middleware.cors import CORSMiddleware

# Importa las librerías de web scraping
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# Permite solicitudes de tu página web (index.html)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción, reemplaza "*" con la URL de tu sitio web
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

kb = SmartKnowledgeBase()

class ChatRequest(BaseModel):
    message: str

def scrape_tipo_cambio():
    """Función para extraer el tipo de cambio de una página web."""
    try:
        url = "https://www.sunat.gob.pe/cl-at-itcambio/tcS01Alias"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscamos en la tabla de la página el valor del tipo de cambio
        # Esta línea es un ejemplo y puede necesitar ser ajustada si la página cambia.
        valor_compra = soup.find('td', class_='valor-compra').text.strip()
        return f"El tipo de cambio actual (compra) es S/ {valor_compra}."
    except Exception:
        return "Lo siento, hubo un error al obtener el tipo de cambio en este momento."

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message.lower()

    # Lógica híbrida:

    # 1. Prioridad: Revisar si la pregunta requiere web scraping
    if "tipo de cambio" in user_message or "dólar" in user_message:
        response = scrape_tipo_cambio()

    # 2. Si no es una pregunta de web scraping, buscar en la base de conocimiento manual
    else:
        response = kb.find_best_answer(user_message)

        # 3. Si tampoco encuentra respuesta, dar una genérica
        if response is None:
            response = "Lo siento, no tengo información sobre eso. Intenta reformular tu pregunta."

    return {"response": response}