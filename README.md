# Projeto Fullstack – FastAPI + React + Docker

Projeto **Fullstack** desenvolvido com **React.js** no frontend e **FastAPI** no backend. O objetivo é integrar frontend e backend, utlizando comunicação via APIs e executando a aplicação com o **Docker**.

## Estrutura do Projeto

```
docker-fullstack/
├─ backend/
│  ├─ main.py
│  ├─ people.json
│  ├─ requirements.txt
│  └─ Dockerfile
│
└─ frontend/
   ├─ src/
   │   └─ App.js
   ├─ public/
   │   └─ index.html
   ├─ package.json
   └─ Dockerfile
```

---

## Funcionalidades

### Backend

#### GET /api01

Retorna uma lista de pessoas utilizando dados fixos no código.

#### GET /api02

Retorna uma lista de pessoas carregadas a partir de um arquivo `people.json`.

---

## Tecnologias Utilizadas

### Backend

* Python
* FastAPI
* Uvicorn
* Docker

### Frontend

* React.js
* Axios
* Docker

---

## Como executar o projeto

As instruções abaixo mostram como rodar a aplicação **localmente** e utilizando **Docker**.

---

## Requisitos

Antes de começar, verifique se você possui:

* Python 3.9 ou superior
* Node.js com npm
* Docker
* Git

---

## Passo inicial

1. Clone o repositório:

```bash
git clone <repositorio>
```

2. Acesse a pasta do projeto:

```bash
cd docker-fullstack
```

3. Verifique se existem as pastas `backend` e `frontend`.

---

## Rodando o Backend (FastAPI)

### Execução local

1. Entre na pasta do backend:

```bash
cd backend
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
```

3. Ative o ambiente virtual:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Inicie o servidor:

```bash
uvicorn main:app --reload
```

O backend estará disponível em:

```
http://localhost:8000
```

---

## Rodando o Frontend (React)

### Execução local

1. Em outro terminal, entre na pasta do frontend:

```bash
cd frontend
```

2. Instale as dependências:

```bash
npm install
```

3. Inicie o servidor de desenvolvimento:

```bash
npm start
```

O frontend ficará acessível em:

```
http://localhost:3000
```

Quando executado localmente, o frontend se comunica com o backend usando:

```
http://localhost:8000
```

---

## Executando com Docker

### Construção das imagens

Na raiz do projeto, execute:

```bash
docker build -t backend_atividade ./backend
docker build -t frontend_atividade ./frontend
```

---

### Criando a rede Docker

```bash
docker network create fullstack
```

---

### Subindo os containers

**Backend:**

```bash
docker run --rm --name backend_atividade --network fullstack -p 8000:8000 backend_atividade
```

**Frontend:**

```bash
docker run --rm --name frontend_atividade --network fullstack -p 3000:3000 frontend_atividade
```

---

## Comunicação entre frontend e backend no Docker

Quando a aplicação estiver rodando via Docker, o frontend deve acessar o backend utilizando o nome do container:

```
http://backend_atividade:8000
```

Isso garante que a comunicação funcione corretamente dentro da rede Docker, sem o uso de `localhost`.
