from flask import Flask, render_template, request
import json

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
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html') 

#cardápio   
@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

#feedback
@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        msg = request.form["mensagem"]
        palavras = msg.split()

        return render_template(
            "feedback_resultado.html",
            mensagem=msg,
            palavras=palavras
        )

    return render_template("feedback.html")


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

