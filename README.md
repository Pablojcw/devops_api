# DevOps API

API REST para gerenciamento de equipamentos, desenvolvida como projeto de estudo
de DevOps. A aplicação permite cadastrar, consultar, atualizar e excluir
equipamentos, armazenando os dados em um banco relacional.

## Objetivo

Praticar o desenvolvimento e a execução de uma API em Python com persistência
de dados, testes automatizados e conteinerização usando Docker.

## Tecnologias utilizadas

- Python 3.13
- Flask
- Flask-SQLAlchemy
- Flasgger, para documentação da API com Swagger
- SQLite, usado por padrão no desenvolvimento e nos testes
- MySQL 8.0, usado no ambiente Docker Compose
- Pytest
- Docker e Docker Compose

## Estrutura de pastas

```text
devops-api/
├── app/
│   ├── __init__.py       # Inicialização do pacote da aplicação
│   ├── main.py           # Fábrica da aplicação e rotas da API
│   └── modelo.py         # Modelo Equipment e configuração do SQLAlchemy
├── instance/             # Arquivos locais da instância da aplicação
├── tests/
│   ├── config.py         # Fixtures de teste
│   ├── conftest.py       # Configuração compartilhada do Pytest
│   └── test_equipment.py # Testes dos endpoints
├── Dockerfile            # Imagem da API
├── docker-compose.yml    # API e banco MySQL
├── requirements.txt      # Dependências Python
└── README.md             # Documentação do projeto
```

## Instalação

### Execução local

1. Clone o repositório e acesse a pasta do projeto.
2. Crie e ative um ambiente virtual:

	```bash
	python -m venv .venv
	```

	No Windows PowerShell:

	```powershell
	.\.venv\Scripts\Activate.ps1
	```

	No Linux ou macOS:

	```bash
	source .venv/bin/activate
	```

3. Instale as dependências:

	```bash
	pip install -r requirements.txt
	```

### Execução com Docker

É necessário ter Docker e Docker Compose instalados. As imagens e os
containers são criados com:

```bash
docker compose up --build
```

## Execução

### API local

Com o ambiente virtual ativado, execute:

```bash
flask --app app run --debug
```

A API ficará disponível em `http://localhost:5000`.

### API com Docker

Ao usar Docker Compose, a API também ficará disponível em
`http://localhost:5000`. O banco MySQL será iniciado automaticamente pelo
serviço `db`.

### Endpoints principais

| Método | Endpoint | Descrição |
| --- | --- | --- |
| `GET` | `/health` | Verifica se a API está funcionando |
| `GET` | `/equipment` | Lista os equipamentos |
| `POST` | `/equipment` | Cadastra um equipamento |
| `GET` | `/equipment/<id>` | Consulta um equipamento |
| `PUT` | `/equipment/<id>` | Atualiza um equipamento |
| `DELETE` | `/equipment/<id>` | Exclui um equipamento |

A documentação interativa do Swagger pode ser acessada em
`http://localhost:5000/apidocs/`.

### Testes

Para executar os testes automatizados:

```bash
pytest
```

## Licença

Este projeto ainda não possui um arquivo de licença definido. Até que uma
licença seja adicionada ao repositório, os direitos de uso, cópia e
distribuição permanecem reservados ao autor.