from flask import Flask, render_template, request, url_for
from utils import db, lm
from flask_migrate import Migrate
from controllers.usuarios import bp_usuarios
#removipizzasepedidos

from flask import render_template

app = Flask(__name__)

conexao = "sqlite:///meubanco.sqlite"

app.config['SECRET_KEY'] = 'minha-chave'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
#removipizzasepedidos

db.init_app(app)
lm.init_app(app)
migrate = Migrate(app, db)

@app.errorhandler(401)
def acesso_negado(e):
    return render_template('acesso_negado.html'), 404


@app.run(host='0.0.0.0', port=81)
