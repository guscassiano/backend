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


## 🧪 Testes Automatizados

Foi incrementado testes automatizados utilizando `pytest` e o `TestClient` do FastAPI para garantir a integridade e o funcionamento correto dos endpoints.

### Pré-requisitos

Antes de rodar os testes, certifique-se de que as dependências de desenvolvimento estão instaladas:

```bash
uv pip install -e ".[dev]"
```

## 📝 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/movies/` | Criar filme |
| GET | `/movies/` | Listar filmes |
| GET | `/movies/{id}` | Buscar filme |
| PUT | `/movies/{id}` | Atualizar filme |
| PATCH | `/movies/{id}` | Atualizar parcialmente filme |
| DELETE | `/movies/{id}` | Deletar filme |
