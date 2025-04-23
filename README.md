# 🧠 Nave IA - Assistente Virtual com OpenAI + Gleap (Piloto)

Este repositório apresenta o projeto-piloto de integração entre a OpenAI Assistants API e o sistema de suporte da plataforma Nave, utilizando como interface visual a "Eva", chatbot embutida via Gleap.

> 🎯 Link para testar a assistente: [https://bit.ly/naveai](https://bit.ly/naveai)

---

## 🚀 Visão Geral

O objetivo deste piloto é:
- Reduzir a abertura de tickets manuais
- Automatizar respostas com base em FAQ oficial
- Melhorar a experiência do usuário com uma IA simpática e empática
- Servir como base para expansão de IA em todos os módulos da Nave

A Eva é integrada a um backend FastAPI que envia mensagens para um agent configurado na OpenAI (Assistants API), que possui:
- 🧠 Instruções personalizadas
- 📎 Arquivo FAQ.md vetorizado
- 💬 Capacidade de conversação natural

---

## 👩‍💻 Tecnologias Utilizadas

- **FastAPI** – API backend
- **OpenAI Assistants API** – LLM com suporte a threads, tools e arquivos
- **Uvicorn** – Servidor ASGI leve
- **Quasar Framework (via CDN)** – Frontend responsivo e moderno
- **Render.com** – Hospedagem gratuita do backend
- **Gleap (Eva)** – Interface visual de chat nativa na Nave

---

## 🧩 Estrutura do Projeto

