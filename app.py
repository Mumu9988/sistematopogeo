from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Sistema Topogeo rodando!'

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    propriedade = request.form['propriedade']
    return f"Produtor {nome} cadastrado com sucesso!"
