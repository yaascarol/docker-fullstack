# Projeto Fullstack – FastAPI + React + Docker

Projeto **Fullstack** desenvolvido com **React.js** no frontend e **FastAPI** no backend. O objetivo é integrar frontend e backend, utlizando comunicação via APIs e executando a aplicação com o **Docker**.

## 📁 Estrutura do Projeto


```text
docker-fullstack/
├─ backend/
│  ├─ main.py
│  ├─ people.json
│  ├─ requirements.txt
│  └─ Dockerfile
│
└─ frontend/
   ├─ src/
   │   └── App.js
   ├─ public/
   │   └── index.html
   ├─ package.json
   └─ Dockerfile

---

## Funcionalidades

**Backend**

### ` GET /api01 `
Retorna uma lista de pessoas utilizando dados fixos no código.

### ` GET /api02 `
Retorna uma lista de pessoas carregadas a partir de um arquivo people.json

---

## Tecnologias Utilizadas

### Backend
- **Python**
- **FastAPI**
- **Uvicorn**
- **Docker**

### Frontend
- **React.js**
- **Axios**
- **Docker**

---

## Como executar o projeto

Abaixo estão as instruções para rodar a aplicação tanto **localmente** quanto usando **Docker**.

---

## Requisitos

Antes de começar, confira se você já possui:

- Python **3.9 ou superior**
- Node.js com **npm**
- Docker
- Git

---

## Passo inicial

1. Faça o clone do repositório:
   ```bash
   git clone <repositorio>

2. Acesse a pasta do projeto:

cd docker-fullstack

3. Verifique se existem as pastas backend e frontend.

## Rodando o Backend (FastAPI)

**Execução local**

1. Entre na pasta do backend:

cd backend

2. Crie um ambiente virtual para evitar conflitos de dependências:

python -m venv venv

3. Ative o ambiente virtual:

**Windows:**

venv\Scripts\activate

**Linux / macOS:**

source venv/bin/activate

4. Instale as dependências do projeto:

pip install -r requirements.txt

5. Inicie o servidor:

uvicorn main:app --reload

O backend estará disponível em:
http://localhost:8000

## Rodando o Frontend (React)

**Execução local**

1. Abra outro terminal e entre na pasta do frontend:

cd frontend

2. Instale as dependências:

npm install

3. Inicie o servidor de desenvolvimento:

npm start

O frontend ficará acessível em:
http://localhost:3000

Quando executar, o frontend se comunicará com o backend usando http://localhost:8000.

## Executando com Docker

**Construção das imagens**

1. Na raiz do projeto, execute:

docker build -t backend_atividade ./backend
docker build -t frontend_atividade ./frontend

2. Criando a rede Docker

Criamos uma rede interna para permitir que os containers se comuniquem entre si:

docker network create fullstack

**Subindo os containers**

1. Inicie o backend:

docker run --rm --name backend_atividade --network fullstack -p 8000:8000 backend_atividade


2. Em outro terminal, inicie o frontend:

docker run --rm --name frontend_atividade --network fullstack -p 3000:3000 frontend_atividade

## Comunicação entre frontend e backend no Docker

Quando a aplicação for rodar via Docker, o frontend precisa acessar o backend usando o nome do container:

http://backend_atividade:8000


Isso garante que a comunicação funcione corretamente dentro da rede Docker, pois os serviços se comunicam pelo nome do container e não por localhost.