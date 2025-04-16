# Python REST API Modernizada

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.78.0-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Repositório: [basic-python-rest-api](https://github.com/jeffthedeveloper/Python-Weekend-Projects/basic-python-rest-api)  
Perfil GitHub: [jeffthedeveloper](https://github.com/jeffthedeveloper)

Exemplo modernizado de como criar uma API REST em Python com FastAPI, incluindo todas as melhores práticas atuais.

## Principais Componentes da API

✅ **Operações CRUD completas**  
✅ **Validação de dados com Pydantic**  
✅ **Logging estruturado**  
✅ **Banco de dados assíncrono**  
✅ **Tratamento de erros padronizado**  
✅ **Documentação automática (Swagger/ReDoc)**  
✅ **Autenticação JWT**  
✅ **Health checks**  
✅ **Testes automatizados**  
✅ **Containerização com Docker**  
✅ **Configuração por ambiente**

## Tecnologias Utilizadas

- 🚀 **FastAPI**: Framework moderno e rápido para construção de APIs
- 🐘 **SQLAlchemy 2.0**: ORM com suporte a async/await
- 🔐 **JWT**: Autenticação segura
- 📊 **Pydantic**: Validação de dados e serialização
- 🐳 **Docker**: Containerização da aplicação
- 📝 **OpenAPI**: Documentação automática
- ✅ **Pytest**: Testes automatizados

## Instalação

### Pré-requisitos

- Python 3.9+
- Docker (opcional)
- Poetry (gerenciador de dependências)

### Configuração Inicial

1. Clone o repositório:

```bash
git clone https://github.com/jeffthedeveloper/Python-Weekend-Projects/basic-python-rest-api.git
cd basic-python-rest-api
```

2. Configure o ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows

pip install poetry
poetry install
```

3. Configure as variáveis de ambiente:

```bash
cp .env.example .env
# Edite o .env conforme necessário
```

## Executando a API

### Modo Desenvolvimento (com live reload):

```bash
uvicorn api.main:app --reload
```

Acesse a documentação interativa:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Com Docker:

```bash
docker-compose up -d --build
```

## Estrutura do Projeto

```
basic-python-rest-api/
├── api/                   # Código fonte da aplicação
│   ├── config/            # Configurações
│   ├── dependencies/      # Injeção de dependências
│   ├── models/            # Modelos de banco de dados
│   ├── routers/           # Endpoints da API
│   ├── schemas/           # Schemas Pydantic
│   ├── services/          # Lógica de negócio
│   ├── tests/             # Testes automatizados
│   └── utils/             # Utilitários
├── .env                   # Variáveis de ambiente
├── docker-compose.yml     # Configuração Docker
├── Dockerfile             # Definição da imagem Docker
├── pyproject.toml         # Dependências e configuração
└── README.md              # Este arquivo
```

## Endpoints Principais

| Método | Endpoint          | Descrição                     |
|--------|-------------------|-------------------------------|
| GET    | /examples         | Lista todos os exemplos       |
| POST   | /examples         | Cria um novo exemplo          |
| GET    | /examples/{id}    | Obtém um exemplo específico   |
| PUT    | /examples/{id}    | Atualiza um exemplo           |
| DELETE | /examples/{id}    | Remove um exemplo             |
| GET    | /health           | Verifica saúde da aplicação   |

## Testes

Para executar os testes:

```bash
pytest
```

## Configuração Avançada

### Variáveis de Ambiente

| Variável                     | Descrição                              | Padrão                          |
|------------------------------|----------------------------------------|---------------------------------|
| DATABASE_URL                 | URL de conexão com o banco de dados    | postgresql+asyncpg://...        |
| SECRET_KEY                   | Chave secreta para JWT                 | secret-key-change-in-production |
| ACCESS_TOKEN_EXPIRE_MINUTES  | Tempo de expiração do token JWT        | 30                              |
| LOG_LEVEL                    | Nível de logging (DEBUG, INFO, etc.)   | INFO                            |

### Banco de Dados

A API suporta PostgreSQL de forma nativa. Para configurar:

1. Instale o PostgreSQL
2. Crie um banco de dados
3. Atualize o `DATABASE_URL` no `.env`

Para migrações de banco de dados, utilizamos Alembic:

```bash
alembic revision --autogenerate -m "descrição da migração"
alembic upgrade head
```

## Contribuição

Contribuições são bem-vindas! Siga os passos:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## Contato

Jeff The Developer - [@jeffthedeveloper](https://github.com/jeffthedeveloper)  
Link do Projeto: [https://github.com/jeffthedeveloper/Python-Weekend-Projects/basic-python-rest-api](https://github.com/jeffthedeveloper/Python-Weekend-Projects/basic-python-rest-api)