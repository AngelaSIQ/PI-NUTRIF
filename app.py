from flask import Flask, render_template

app = Flask(__name__)

#pagina inicial
@app.route('/')
def index():
    return render_template('index.html')

#login
@app.route('/login')
def login():
    return render_template('login.html')   

#cadastro
@app.route('/cadastro/<usuario>')
def cadastro(usuario):
    return render_template('cadastro.html') 

#cardápio   
@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

#feedback
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')   

#receitas
@app.route('/receitas/<prato>')
def receitas():
    return render_template('receitas.html') 

#contatos
@app.route('/contatos')
def contato():
    return render_template('contatos.html')    


if __name__ == "__main__":    
    app.run()

