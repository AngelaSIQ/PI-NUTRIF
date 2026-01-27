from flask import Flask, render_template, request, url_for
import json
from flask import flash, redirect
from utils import db
import os
from flask_migrate import Migrate
from models import Usuario


app = Flask(__name__)
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_mydb = os.getenv('DB_DATABASE')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}:{db_port}/{db_mydb}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


#pagina inicial
@app.route('/')
def index():
    return render_template('index.html')

#login
@app.route('/login')
def login():
    return render_template('login.html')   

# #cadastro
# @app.route('/cadastro')
# def cadastro():
#     return render_template('cadastro.html') 

@app.route('/cadastroaluno')
def cadastroaluno():
    return render_template('cadastroaluno.html') 

@app.route('/cadastroservidor')
def cadastroservidor():
    return render_template('cadastroservidor.html') 

@app.route('/perfilservidor')
def perfilservidor():
    return render_template('perfilservidor.html') 

@app.route('/perfilusuario')
def perfilusuario():
    return render_template('perfilusuario.html') 

#cardápio   
@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

#feedback
feedbacks_lista = []
@app.route("/feedback", methods=['POST'])
def feedback():
    msg = request.form.get('mensagem')
    feedbacks_lista.append(msg)
    return redirect(url_for("feedback_resultados"))

@app.route("/feedback_form")
def feedback_form():
    return render_template("feedback.html")

@app.route("/feedback_resultados")
def feedback_resultados():  # ✔ NOME ARRUMADO
    return render_template("feedback_resultados.html", mensagem=feedbacks_lista)  # ✔ RETURN adicionado

#receitas
@app.route('/receitas')
def receitas():
    return render_template('receitas.html') 

@app.route('/prato')
def prato():
    return render_template('prato.html') 

#contatos
@app.route('/contatos')
def contato():
    return render_template('contatos.html')   

#restricao
@app.route('/restricao')
def restricao():   
    return render_template('restricao.html')  



if __name__ == "__main__":    
    app.run()
