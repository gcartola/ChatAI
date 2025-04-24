🧠 Nave IA - Assistente Virtual com OpenAI + Gleap (Piloto)

Este repositório apresenta um projeto-piloto que integra a API de Assistants da OpenAI com a plataforma de atendimento Gleap, criando uma interface de suporte inteligente aos usuários da Nave. O objetivo é oferecer respostas imediatas baseadas em FAQ antes da abertura de um chamado.

🚀 Visão Geral

A assistente "Eva" atua como uma interface visual de chat, conectando-se ao backend que utiliza a OpenAI Assistants API para processar mensagens e responder com base em:

📄 FAQ estruturado da Nave (arquivo markdown)

⚖️ Instruções contextuais configuradas no Assistant

🧬 Interação natural por linguagem humana

🔧 Tecnologias Utilizadas

FastAPI: Backend leve e performático em Python

OpenAI Assistants API: Gerenciamento de agentes com memória, funções e busca em arquivos

Uvicorn: Servidor ASGI para execução local

Gleap (Eva): Interface visual de atendimento integrada ao frontend

📊 Objetivos do Projeto

🔻 Reduzir o volume de tickets manuais

🚀 Aumentar a autonomia do usuário

⚛️ Integrar IA nativamente ao fluxo da Nave

📏 Criar base para futuras aplicações com IA generativa

📁 Estrutura do Repositório

├── backend/
│   ├── main.py              # Endpoint FastAPI que aciona a Assistants API
│   ├── requirements.txt     # Dependências Python do backend
│
├── frontend/
│   └── gleap_integration.js # Simula a integração com o Gleap
│
├── docs/
│   └── FAQ.md               # Conteúdo base usado pelo Assistant
│
├── .env                     # Chaves e variáveis sensíveis
├── README.md                # Este documento

🚧 Setup Local para Desenvolvedores

# 1. Clonar o repositório
git clone https://github.com/gcartola/nave-ia-suporte-piloto.git
cd nave-ia-suporte-piloto

# 2. Criar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Instalar dependências
pip install -r backend/requirements.txt

# 4. Criar arquivo .env com:
OPENAI_API_KEY=sk-...
ASSISTANT_ID=asst_...

# 5. Subir o servidor
uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload

A API ficará acessível em:

POST http://localhost:8000/ia-suporte

🚹 Integração com a Eva (Gleap)

O que o Gleap oferece:

🖊️ Chat visual com o usuário

⚖️ Webhook customizável para envio das mensagens

Configuração no Gleap:

Acesse: Settings > Eva > Webhook URL

Informe: https://api.nave.com.br/ia-suporte

Payload enviado pela Eva:

{
  "mensagem": "Como acessar meus contratos?"
}

Resposta da IA (automática):

{
  "resposta": "Para visualizar seus contratos, acesse o menu lateral..."
}

🛠️ Funcionamento Interno do Backend

Cria uma thread para cada interação

Adiciona a mensagem recebida nessa thread

Executa um run com base no assistant_id

Aguarda com polling até que o status seja completed

Retorna a resposta gerada pelo modelo

📊 Benefícios Esperados

Antes:

❌ Todos os atendimentos geravam tickets

⚡️ Usuários frustrados

⛔ Suporte sobrecarregado

Depois:

📈 Redução de 60 a 70% nos tickets

🤪 Respostas empáticas e em linguagem natural

✅ Suporte focado em casos críticos

📊 Métricas sobre intencionalidade

📖 Arquitetura do Assistant

Modelo: gpt-4

Ferramentas: File Search (vetor com o FAQ)

Instruções do sistema:

Atue como um atendente treinado para responder perguntas sobre o sistema Nave. Use apenas informações do FAQ. Oriente o usuário a abrir um chamado se não tiver certeza da resposta.

🌍 Roadmap Futuro



🙏 Contribuições

Pull requests são bem-vindos! Para sugestões ou bugs, abra uma issue ou entre em contato com o mantenedor.

Feito com ❤️ para melhorar a experiência dos nossos usuários e empoderar o time de suporte da Nave.
