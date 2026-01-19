from flask import Blueprint
from flask import render_template, request, redirect, flash
from models import Usuario
from utils import db, lm
from flask_login import login_user, logout_user, login_required

bp_usuarios = Blueprint('usuarios', __name__)


class Usuario(db.Model, UserMixin):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return "Usuario: {}".format(self.nome)


@bp_usuarios.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    u = Usuario.query.get(id)
    if request.method == 'GET':
        return render_template('usuarios_delete.html', u=u)

    if request.method == 'POST':
        db.session.delete(u)
        db.session.commit()
        return 'Dados excluídos com sucesso'


@login_manager.user_loader
def load_user(id):
    usuario = Usuario.query.filter_by(id=id).first()
    return usuario


@bp_usuarios.route('/autenticar', methods=['POST'])
def autenticar():
    email = request.form.get('email')
    senha = request.form.get('senha')
    usuario = Usuario.query.filter_by(email=email).first()

    if usuario and (senha == usuario.senha):
        login_user(usuario)
        return redirect('recovery')
    else:
        flash('Dados incorretos')
        return redirect('/')


@bp_usuarios.route('/logoff')
def logoff():
    logout_user()
    return redirect('/')


@bp_usuarios.route('/')
@bp_usuarios.route('/recovery')
@login_required
def recovery():
    usuarios = Usuario.query.all()
    return render_template('usuarios/usuarios_recovery.html', usuarios=usuarios)
