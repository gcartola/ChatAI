from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class UserMessage(BaseModel):
    mensagem: str

@app.post("/ia-suporte")
async def ia_suporte(request: UserMessage):
    response = client.beta.threads.create_and_run(
        assistant_id="asst_SEU_ID_AQUI",
        thread={"messages": [{"role": "user", "content": request.mensagem}]}
    )
    return {"resposta": response.run.response.message.content}