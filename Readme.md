<p align="center">
  <img src="./assets/images/python.png" width="300" alt="Python" /></a>
</p>

## Telas do sistema:
<p align="center">
  <img src="./assets/images/crud.png" width="800" alt="Tela CRUD Cidades" /></a>
</p>
<p align="center">
  <img src="./assets/images/mapa.png" width="800" alt="Modelo Mapa" /></a>
</p>

## criando o banco
```bash
docker run --name postgres-db -e POSTGRES_PASSWORD=SUA_SENHA_AQUI -p 5432:5432 -d postgres
```
## Gerando as tabelas
```bash
CREATE TABLE public.cidade_brasil (
	id serial4 NOT NULL,
	estado varchar(255) NULL,
	nome_estado varchar(255) NULL,
	cidade varchar(255) NULL,
	codigo_cidade varchar(255) NULL,
	codigo_estado varchar(255) NULL,
	população varchar(255) NULL,
	regiao varchar(255) NULL,
	coordenada varchar(255) NULL,
	parceiros varchar(255) NULL,
	criado_por varchar(255) NULL,
	criado_em varchar(255) NULL,
	alterado_por varchar(255) NULL,
	alterado_em varchar(255) NULL,
	etag varchar(255) NULL,
	CONSTRAINT cidade_brasil_pkey PRIMARY KEY (id)
);

CREATE TABLE public.tecnico (
	id serial4 NOT NULL,
	nome varchar(30) NOT NULL,
	id_cidade int8 NOT NULL,
	criado_por int8 NULL,
	criado_em timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	nota_media varchar(30) NULL,
	coordenada varchar(255) NULL,
	alterado_por int8 NULL,
	alterado_em timestamp NULL,
	etag int4 NOT NULL DEFAULT 1,
	CONSTRAINT tecnico_pkey PRIMARY KEY (id)
);
```

## Criando o projeto env
```bash
python3 -m venv projetoCrud
```

## Ativando o projeto
```bash
source bin/activate
```

## instala a conexão com postgre
```bash
pip install psycopg2
```

## instale o flask
```bash
pip install flask
```

## rodar o projeto
```bash
falsk run
```
