from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

# Carrega variáveis do .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
assistant_id = os.getenv("ASSISTANT_ID")

app = FastAPI()

class UserMessage(BaseModel):
    mensagem: str

# Rota raiz que retorna o index.html
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app.mount("/", StaticFiles(directory="backend", html=True), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return FileResponse("backend/index.html")

# Endpoint principal da IA
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
                return {"erro": "A IA falhou ao processar sua dúvida. Tente novamente ou abra um chamado."}
            elif time.time() - start > max_wait:
                return {"erro": "⏳ Tempo de resposta excedido. Tente novamente mais tarde."}

            time.sleep(1)

        messages = client.beta.threads.messages.list(thread_id=thread.id)
        resposta = None

        for m in messages.data:
            if m.role == "assistant":
                resposta = m.content[0].text.value
                break

        if not resposta:
            return {"erro": "⚠️ Nenhuma resposta foi retornada pela IA."}

        return {"resposta": resposta}

    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}
