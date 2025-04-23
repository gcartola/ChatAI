from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

# Carrega as variáveis do .env
load_dotenv()

# Inicializa o cliente da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
assistant_id = os.getenv("ASSISTANT_ID")

# Inicializa a aplicação FastAPI
app = FastAPI()

# Monta arquivos estáticos (logo, CSS customizado, etc)
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# Template engine
templates = Jinja2Templates(directory="backend")

# Define o modelo da mensagem recebida
class UserMessage(BaseModel):
    mensagem: str

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ia-suporte")
async def ia_suporte(request: UserMessage):
    print("📩 Mensagem recebida:", request.mensagem)
    print("🧠 Assistant ID:", assistant_id)

    try:
        thread = client.beta.threads.create()
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=request.mensagem
        )

        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id
        )

        max_wait = 60
        start = time.time()

        while True:
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )

            if run_status.status == "completed":
                break
            elif run_status.status == "failed":
                print("❌ Agent falhou:", run_status)
                return JSONResponse(status_code=500, content={"resposta": "A IA falhou ao processar sua dúvida. Tente novamente ou abra um chamado."})
            elif time.time() - start > max_wait:
                return JSONResponse(status_code=504, content={"resposta": "⏳ Tempo de resposta excedido. Tente novamente mais tarde."})

            time.sleep(1)

        messages = client.beta.threads.messages.list(thread_id=thread.id)
        resposta = next((m.content[0].text.value for m in messages.data if m.role == "assistant"), None)

        if not resposta:
            return JSONResponse(status_code=404, content={"resposta": "⚠️ Nenhuma resposta foi retornada pela IA."})

        print("✅ Resposta gerada:", resposta)
        return {"resposta": resposta}

    except Exception as e:
        print("⚠️ Erro inesperado:", e)
        return JSONResponse(status_code=500, content={"resposta": f"Erro inesperado: {str(e)}"})
