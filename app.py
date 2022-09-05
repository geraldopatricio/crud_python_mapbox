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

@app.route('/mapa')
def mapalist():
    return render_template("mapa.html", map = map)

if(__name__ == "__main__"):
    app.run()
    
