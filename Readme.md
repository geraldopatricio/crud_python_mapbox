## criando o banco
docker run --name postgres-db -e POSTGRES_PASSWORD=odlareg -p 5432:5432 -d postgres

## Criando o projeto env
python3 -m venv projetoCrud

## Ativando o projeto
source bin/activate

## instala a conexão com postgre
pip install psycopg2

## instale o flask
pip install flask

## rodar o projeto
falsk run
