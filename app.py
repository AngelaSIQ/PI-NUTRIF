from flask import Flask, render_template, request

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
@app.route("/feedback", methods=['POST'])
def feedback():
    msg = request.form['obrigada']
    feedbacks_lista.append(msg)
    return
    redirect(url_for("feedback_resultados"))
   

@app.route("/feedback_form")
def feedback_form():
    return render_template("feedback.html")

@app.route("/feedback_resultados")
def feddback_resultados():
    render_template("feedback_resultados.html", feedbacks=feedbacks_lista)
    
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
def contato():
    return render_template('restricao.html')  

if __name__ == "__main__":    
    app.run()
