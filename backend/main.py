from fastapi import FastAPI
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

# Modelo esperado na requisição
class UserMessage(BaseModel):
    mensagem: str

@app.post("/ia-suporte")
async def ia_suporte(request: UserMessage):
    print("📩 Mensagem recebida:", request.mensagem)
    print("🧠 Assistant ID:", assistant_id)

    try:
        # 1. Cria a thread
        thread = client.beta.threads.create()

        # 2. Adiciona a mensagem do usuário
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=request.mensagem
        )

        # 3. Executa o agent
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id
        )

        # 4. Polling até finalizar
        while True:
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )

            if run_status.status == "completed":
                break

            elif run_status.status == "failed":
                print("❌ Agent falhou:")
                print(run_status)  # imprime detalhes do erro
                return {"erro": "Falha na execução do agent. Veja detalhes no terminal."}

            time.sleep(1)

        # 5. Busca a resposta do agent
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        resposta = messages.data[0].content[0].text.value

        print("✅ Resposta gerada:", resposta)
        return {"resposta": resposta}

    except Exception as e:
        print("⚠️ Erro inesperado:", e)
        return {"erro": f"Ocorreu um erro inesperado: {str(e)}"}
