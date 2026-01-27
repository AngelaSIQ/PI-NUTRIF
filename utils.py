from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
lm = LoginManager()

from flask import Flask, render_template
from utils import db, lm
from flask_migrate import Migrate
from controllers.usuarios import bp_usuarios
#removi o pizzas e pedidos

from flask import render_template

app = Flask(__name__)

conexao = "sqlite:///meubanco.sqlite"

app.config['SECRET_KEY'] = 'minha-chave'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')
#removi o pizzas e pedidos

db.init_app(app)
lm.init_app(app)
migrate = Migrate(app, db)