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

Após a instalação as dependências de desenvolvimento executar:

```bash
uv run pytest
```

Observação: Certificar de ter instalado o geranciador de pacote uv para a execução local na máquina, para o Docker não é necessário.


## ✨ Qualidade de Código e Padronização

Para garantir um código limpo, legível e padronizado, o projeto utiliza um *pipeline* de qualidade de código com as seguintes ferramentas:

* **Black**: Formatador de código automático e opinativo.
* **Flake8**: Linter para checagem de estilo (PEP 8) e detecção de erros.
* **pre-commit**: Ferramenta que gerencia e executa o Black e o Flake8 automaticamente antes de cada `git commit`.

Isso garante que todo o código enviado ao repositório siga os mesmos padrões de qualidade, de forma automatizada.

### 🔧 Ativando os Hooks Localmente

Para que o `pre-commit` valide seu código automaticamente *antes* de cada commit na sua máquina, você precisa ativar os "hooks" do git.

1.  Primeiro, certifique-se de que as dependências de desenvolvimento estão instaladas (o que também instala o pacote `pre-commit`):
    ```bash
    uv pip install -e ".[dev]"
    ```

2.  Em seguida, ative os hooks no seu repositório local:
    ```bash
    uv run pre-commit install
    ```

A partir de agora, a cada `git commit`, as validações rodarão automaticamente baseado nas configurações do arquivo `.pre-commit-config.yaml`.


## 📝 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/movies/` | Criar filme |
| GET | `/movies/` | Listar filmes |
| GET | `/movies/{id}` | Buscar filme |
| PUT | `/movies/{id}` | Atualizar filme |
| PATCH | `/movies/{id}` | Atualizar parcialmente filme |
| DELETE | `/movies/{id}` | Deletar filme |
