🧠 Nave IA - Assistente Virtual com OpenAI + Gleap (Piloto)

Este repositório apresenta um projeto-piloto que integra a API de Assistants da OpenAI com a plataforma de atendimento Gleap, criando uma interface de suporte inteligente aos usuários da Nave. O objetivo é oferecer respostas imediatas baseadas em FAQ antes da abertura de um chamado.

Acesse a demonstração online: 👉 https://bit.ly/naveai

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

Quasar + HTML + JS: Interface interativa responsiva e moderna

Render.com: Hospedagem gratuita e fácil de configurar para o backend

📊 Objetivos do Projeto

🔻 Reduzir o volume de tickets manuais

🚀 Aumentar a autonomia do usuário

⚛️ Integrar IA nativamente ao fluxo da Nave

📏 Criar base para futuras aplicações com IA generativa

📁 Estrutura do Repositório

├── backend/
│   ├── main.py              # Endpoint FastAPI que aciona a Assistants API
│   ├── requirements.txt     # Dependências Python do backend
│   ├── static/
│   │   └── imagem.png       # Logo exibida no frontend
│
├── frontend/
│   └── index.html           # Interface de chat responsiva (Quasar + JS)
│
├── docs/
│   └── FAQ.md               # Conteúdo base usado pelo Assistant
│
├── .env                     # Chaves e variáveis sensíveis
└── README.md                # Este documento

🚧 Setup Local para Desenvolvedores

# 1. Clonar o repositório
git clone https://github.com/gcartola/nave-ia-suporte-piloto.git
cd nave-ia-suporte-piloto

# 2. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# 3. Instalar dependências
pip install -r backend/requirements.txt

# 4. Criar arquivo .env com:
OPENAI_API_KEY=sk-...
ASSISTANT_ID=asst_...

# 5. Subir o servidor
uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload

A API ficará acessível em:

POST http://localhost:8000/ia-suporte

🛠️ Funcionamento Interno do Backend

Cria uma thread para cada interação

Adiciona a mensagem recebida nessa thread

Executa um run com base no assistant_id

Aguarda com polling até que o status seja completed

Retorna a resposta gerada pelo modelo

🧪 Funcionalidades do Frontend

Interface responsiva (mobile/desktop)

Integração com backend usando fetch

Histórico de conversa salvo em localStorage

Loading com "EVA está digitando..."

Botão "Encerrar conversa" para limpar histórico

Formatação automática de respostas (negrito, itálico, quebra de linha)

📊 Benefícios Esperados

Antes:

❌ Todos os atendimentos geravam tickets

⚡️ Usuários frustrados

⛔ Suporte sobrecarregado

Depois:

📈 Redução de 60 a 70% nos tickets

🤗 Respostas empáticas e em linguagem natural

✅ Suporte focado em casos críticos

📊 Métricas sobre intencionalidade

📖 Arquitetura do Assistant

Modelo: gpt-4

Ferramentas: File Search com FAQ vetorizado

Instruções:

Atue como um atendente treinado para responder perguntas sobre o sistema Nave. Use apenas informações do FAQ. Oriente o usuário a abrir um chamado se não tiver certeza da resposta.

🌍 Roadmap Futuro



🙏 Contribuições

Pull requests são bem-vindos! Para sugestões, melhorias ou bugs, abra uma issue ou entre em contato com o mantenedor.

Feito com ❤️ para melhorar a experiência dos usuários e empoderar o suporte da Nave.



🙏 Contribuições

Pull requests são bem-vindos! Para sugestões ou bugs, abra uma issue ou entre em contato com o mantenedor.

Feito com ❤️ para melhorar a experiência dos nossos usuários e empoderar o time de suporte da Nave.
