# Nave IA Suporte Piloto

Este repositório contém o projeto-piloto de integração entre a API de Assistentes da OpenAI e o sistema Gleap, com o objetivo de automatizar atendimentos aos usuários da plataforma **Nave** antes da abertura de chamados.

A implementação permite que a "Eva" (IA do Gleap) funcione como interface visual, enquanto um agente de linguagem (LLM) no backend realiza o processamento da mensagem e fornece uma resposta inteligente, com base em:

- Dados de FAQ estruturado
- Instruções contextuais do módulo de suporte
- Capacidade de interação natural com linguagem humana

---

## 🚀 Objetivos do Projeto

- Reduzir o volume de tickets abertos manualmente
- Melhorar a experiência de autoatendimento do usuário
- Integrar os agentes da OpenAI ao fluxo nativo da Nave
- Criar base para futuras aplicações de IA nos módulos da plataforma

---

## 📁 Estrutura do Repositório

```
├── backend/
│   ├── main.py              # FastAPI com endpoint que processa as mensagens via Assistants API
│   ├── requirements.txt     # Dependências do backend
│
├── frontend/
│   └── gleap_integration.js # Simula o ponto de integração entre Eva e o backend
│
├── docs/
│   └── FAQ.md               # Conteúdo usado como base para resposta via IA
│
├── .env                     # Variáveis de ambiente (OpenAI API Key, ID do assistant)
├── README.md                # Este arquivo
```

---

## 🫠 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/): API leve e performática em Python
- [OpenAI Assistants API](https://platform.openai.com/docs/assistants): Cria e gerencia agentes com memória, funções e arquivos
- [Uvicorn](https://www.uvicorn.org/): Servidor ASGI para desenvolvimento local
- [Gleap](https://gleap.io/): Plataforma de feedback e atendimento integrada ao frontend

---

## 🚧 Setup e Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/gcartola/nave-ia-suporte-piloto.git
cd nave-ia-suporte-piloto
```

### 2. Criar ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Instalar dependências
```bash
pip install -r backend/requirements.txt
```

### 4. Criar o arquivo `.env`
```
OPENAI_API_KEY=sk-...
ASSISTANT_ID=asst_...
```

### 5. Subir o servidor
```bash
uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

O endpoint estará em:
```
POST http://localhost:8000/ia-suporte
```

---

## 🚩 Integração com o Gleap (Eva)

### ✅ O que o Gleap oferece:
- Interface de chat com usuário final (Eva)
- Permite acionar webhooks personalizados

### ⚖️ Passo a passo da integração

1. No Gleap, acesse: **Settings > Eva > Webhook URL**
2. Informe o endpoint da API local ou deployado:
```http
https://api.nave.com.br/ia-suporte
```
3. A Eva enviará a pergunta do usuário via POST no formato:
```json
{
  "mensagem": "Como acessar meus contratos?"
}
```
4. A resposta da IA (via Assistants API) será retornada automaticamente no mesmo chat.

---

## 🌐 Funcionamento Interno do Backend

- O backend cria uma **thread** por requisição
- Adiciona a mensagem do usuário nessa thread
- Executa um **run** com base no ID do assistant
- Aguarda com polling até que o run esteja `completed`
- Retorna a primeira mensagem de resposta gerada pela IA

---

## 📊 Benefícios Esperados

### Antes:
- 100% dos atendimentos geram ticket
- Usuários impacientes e frustrados
- Suporte sobrecarregado

### Depois da IA:
- Redução estimada de 60 a 70% nos tickets
- Respostas empáticas, contextuais e em linguagem natural
- Suporte focado em problemas críticos
- Métricas sobre intencionalidade e volume de dúvidas

---

## 🔄 Roadmap Futuro

- [ ] Integração com múltiplos agents (um por módulo da Nave)
- [ ] Adição de RAG (retrieval-augmented generation) com documentos internos
- [ ] Expansão para outros canais (WhatsApp, e-mail, etc.)
- [ ] Treinamento do modelo com base nos tickets existentes

---

## 🙏 Contribuição
Pull requests são bem-vindos! Se você tiver dúvidas ou sugestões, abra uma issue ou entre em contato com o mantenedor do repositório.

---

Feito com ❤️ para melhorar a experiência dos nossos clientes e aliviar o time de suporte da Nave.