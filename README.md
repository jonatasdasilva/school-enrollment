# API School Enrollment

![alt text](image.png)

Este projeto busca desenvolver um API básica, para solucionar o problema das matrículas dos alunos da escola **Pequenas Crianças**.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg)](https://www.python.org/downloads/release/python-3130/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.14-blue.svg)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.41-blue.svg)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/Alembic-1.16.2-blue.svg)](https://alembic.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.11.7-blue.svg)](https://pydantic-docs.helpmanual.io/)
[![Pydantic Settings](https://img.shields.io/badge/Pydantic%20Settings-2.10.1-blue.svg)](https://pydantic-settings.helpmanual.io/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.35.0-blue.svg)](https://www.uvicorn.org/)

## Motivação

A escola **Pequenas Crianças** atualmente mantém o controle de seus alunos em **_arquivos físicos_** armazenados na diretoria. No ano letivo anterior, a escola enfrentou problemas de infiltrações e parte dos arquivos dos alunos teve que ser refeita. Considerando isso, a escola decidiu criar um sistema para armazenar as informações dos alunos matriculados.

A solução para a questão foi o desenvolvimento de uma API que permita a matrícula dos alunos da escola, recebendo como entrada as seguintes informações:

- Nome do aluno
- Idade do aluno
- Nome do responsável
- Turma do aluno

**Diferenciais**: Implementação completa do CRUD (Create, Read, Update, Delete).

## Requisitos

Os requisitos aqui elecados são mínimos e necessários para o funcionamento correto do sistema.

- 🟣 **Linux** ou _Windows_
- 🟣 Python 3.13.5+
- 🟣 PostgreSQL
- 🟣 Docker
- 🟣 Docker Compose

## API

A API foi desenvolvida utilizando o framework **FastAPI**, que é um framework moderno, rápido (com alto desempenho) e robusto, baseado em **Starlette** e **Pydantic**.

### Pacotes necessários

- 🟢 Uvicorn
- 🟢 FastAPI
- 🟢 Alembic
- 🟢 Pydantic
- 🟢 SQLAlchemy
- 🟢 Psycopg2-binary
- 🟢 Pydantic Settings

### Estrutura do projeto

A estrutura do projeto é a seguinte:

```bash
school-enrollment/
├── api/
│   ├── __init__.py
│   ├── server.py
│   └── routes/
│       ├── __init__.py
│       ├── database.py
│       ├── models.py
│       ├── routes.py
│       └── settings.py
├── migrations/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── 001_create_students_table.py
├── .dockerignore
├── .env
├── .gitattributes
├── .gitignore
├── alembic.ini
├── docker-compose.yaml
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt

```

### Endpoints

| Endpoint         | Método   | Input          | Descrição             | Retorno          |
| ---------------- | -------- | -------------- | --------------------- | ---------------- |
| `/students`      | `GET`    | None           | Lista todos os alunos | Lista de alunos  |
| `/students`      | `POST`   | Body Json data | Cria um novo aluno    | Aluno criado     |
| `/students/{id}` | `PATCH`  | Body Json data | Atualiza um aluno     | Aluno atualizado |
| `/students/{id}` | `DELETE` | None           | Exclui um aluno       | Aluno excluído   |

> [!IMPORTANT]
> Deve-se observar os dados enviados para que o funcionamento decorra como o esperado.
>
> O objeto json deve ter a seguinte estutura:
>
> ```json
> {
>   "name": "Nome do aluno",
>   "age": "Idade do aluno",
>   "classroom": "Turma do aluno",
>   "responsible": "Nome do responsável"
> }
> ```

### Documentação completa dos endpoits

Para visualizar a documentação completa dos endpoits, basta abrir o navegador e acessar a URL `http://localhost:8778/docs`.

## Execução

Pra executar e testar a solução, basta esscolher uma das formas abaixo.

1. Usando Docker e docker-compose:
   - executar o comando: `docker compose up -d`;
   - realizar consulta na API usando algum utilitário como `curl`: `curl http://localhost:8778/students`.
2. Usando Python 3 local:
   - iniciar o banco de dados: `alembic upgrade head`;
   - editar o arquivo `.env` para configurar a URL do banco de dados (**DATABASE_URL**);
   - a porta de acesso a base de dados, com localhost é a `5454` para o contêiner docker e na rede docker é a `5432`, em caso de uso diferente faz-se necessário inserir a porta correta de acesso;
   - executar o comando: `python3 api/server.py`;
   - realizar consulta na API usando algum utilitário como `curl`: `curl http://localhost:8778/students`.

#### Gerando base de dados

Para gerar a tabela da base de dados será necessário criar a base de dados: `school-enrollment`, e nela a criar da tabela `students`. O DDL para criação da tabela `students`, é constante abaixo e o script de criação via `alembic` está no arquivo `migrations/versions/6b8b2a1a6bf2_create_table_student.py`.

```sql
-- public.students definição

-- Drop table

-- DROP TABLE public.students;

CREATE TABLE public.students (
	id serial4 NOT NULL,
	name varchar NOT NULL,
	age int4 NOT NULL,
	classroom varchar NOT NULL,
	responsible varchar NOT NULL,
	created_at timestamp DEFAULT now() NOT NULL,
	CONSTRAINT student_unique UNIQUE (name, responsible),
	CONSTRAINT students_pkey PRIMARY KEY (id)
);
```

Caso queira realizar modificações na estrutura, e utilizar o `alembic` para gerar a migração, será necessário seguir alguns passos.

Para criar a migração com `alembic` basta executar o comando:

```bash
alembic revision --autogenerate -m "commit da migração"
```

Depois de criar a migração, para enviar basta executar o comando:

```bash
alembic upgrade head
```

Para reverter a última migração aplicada no banco de dados, movendo o histórico de migrações para a versão anterior, basta executar o comando:

```bash
alembic downgrade -1
```

## Conclusão

Com o desenvolvimento da API, foi possível resolver o problema da escola **Pequenas Crianças** de forma eficiente e eficaz.

Permitindo que a escola tenha um controle mais organizado e eficiente dos alunos matriculados, bem como uma melhor gestão dos dados dos alunos.

---

Projeto desenvolvido por [Jônatas da Silva](https://github.com/jonatasdasilva), como parte do teste técnico do vaga de Desenvolvedor Júnior da Faculdade Bahiana de Medicina.
