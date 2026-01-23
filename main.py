from utils import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
  __tablename__="usuario"
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

@app.errorhandler(401)
def acesso_negado(e):
    return render_template('acesso_negado.html'), 404


@app.run(host='0.0.0.0', port=81)