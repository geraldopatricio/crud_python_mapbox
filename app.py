from multiprocessing.connection import Connection
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

def connection():
    s = 'localhost' 
    d = 'amazonlabs' 
    u = 'postgres'
    p = 'odlareg' 
    conn = psycopg2.connect(host=s, user=u, password=p, database=d)
    return conn

## Tela de Login
@app.route('/')
def login():
    return render_template("login.html", login = login)

## listar usuarios
@app.route("/usuarios")
def usuarios():
    users = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    for row in cursor.fetchall():
        users.append({"id": row[0], "usuario": row[1], "criado_em": row[2], "alterado_em": row[3]})
    conn.close()
    return render_template("usuarios.html", users = users)


## cadastrar usuarios
@app.route("/usuario_add", methods = ['GET','POST'])
def usuario_add():
    if request.method == 'GET':
        return render_template("usuario_add.html", user = {})
    if request.method == 'POST':
        id = int(request.form["id"])
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        criado_em = request.form["criado_em"]
        alterado_em = request.form["alterado_em"]
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuario (id, usuario, senha, criado_em, alterado_em) VALUES (%s, %s, %s, %s)", (id, usuario, senha, criado_em, alterado_em))
        conn.commit()
        conn.close()
        return redirect('/usuarios')
    

## listar tecnicos
@app.route("/tecnicos")
def tecnicos():
    tecs = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tecnico")
    for row in cursor.fetchall():
        tecs.append({"id": row[0], "id_cidade": row[1], "nome": row[2], "nota_media": row[3]})
    conn.close()
    return render_template("tecnicos.html", tecs = tecs)

## listar atendimentos
@app.route("/atendimentos")
def atendimentos():
    atends = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM atendimento")
    for row in cursor.fetchall():
        atends.append({"id": row[0], "id_cliente": row[1], "id_tecnico": row[2], "dt_cad": row[3], "dt_close": row[4], "descricao": row[5], "nota": row[6], "status": row[7]})
    conn.close()
    return render_template("atendimentos.html", atends = atends)

## listar cidades
@app.route("/cidades")
def main():
    cids = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cidade_brasil")
    for row in cursor.fetchall():
        cids.append({"id": row[0], "cidade": row[3], "estado": row[1], "regiao": row[7], "populacao": row[6], "coordenada": row[8]})
    conn.close()
    return render_template("cidades.html", cids = cids)

## listar Rotas no Mapa
@app.route('/rota')
def roda():
    return render_template("rota.html")

## Consulta de Técnicos Disponíveis
@app.route('/consulta')
def consulta():
    return render_template("consulta.html")

if(__name__ == "__main__"):
    app.run()
    