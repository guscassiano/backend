# 🎬 Movie API

API RESTful para gerenciamento de filmes construída com FastAPI, SQLAlchemy e Docker.

## 🚀 Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para Python
- **SQLite** - Banco de dados
- **Pydantic** - Validação de dados
- **Docker** - Containerização
- **uv** - Gerenciador de pacotes Python ultrarrápido

## 📦 Instalação

### Com Docker (Recomendado)
```bash
docker-compose up
```

### Sem Docker
```bash
uv sync
uv run uvicorn app.main:app --reload --port 8000
```

## 📚 Documentação

Acesse a documentação interativa:
- Swagger UI: http://localhost:8000/docs


## 📝 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/movies/` | Criar filme |
| GET | `/movies/` | Listar filmes |
| GET | `/movies/{id}` | Buscar filme |
| PUT | `/movies/{id}` | Atualizar filme |
| PATCH | `/movies/{id}` | Atualizar parcialmente filme |
| DELETE | `/movies/{id}` | Deletar filme |
