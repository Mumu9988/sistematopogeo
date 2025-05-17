from flask import Flask, render_template, request, redirect, session
from banco import criar_banco, inserir_produtor, listar_produtores
import os

app = Flask(__name__)
app.secret_key = 'chave-topogeo123'  # Protege a sessão de login
criar_banco()

@app.route('/')
def home():
    return "Sistema Topogeo rodando!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        if request.form['usuario'] == 'admin' and request.form['senha'] == '1234':
            session['logado'] = True
            return redirect('/painel')
        else:
            erro = 'Usuário ou senha incorretos'
    return render_template('login.html', erro=erro)

@app.route('/logout')
def logout():
    session.pop('logado', None)
    return redirect('/login')

@app.route('/cadastro', methods=['GET'])
def cadastro():
    if not session.get('logado'):
        return redirect('/login')
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    if not session.get('logado'):
        return redirect('/login')
    nome = request.form['nome']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    propriedade = request.form['propriedade']
    inserir_produtor(nome, cpf, telefone, propriedade)
    return f"Produtor {nome} cadastrado com sucesso!"

@app.route('/listar')
def listar():
    if not session.get('logado'):
        return redirect('/login')
    produtores = listar_produtores()
    html = "<h1>Produtores Cadastrados</h1><ul>"
    for p in produtores:
        html += f"<li>{p[0]} – CPF: {p[1]} – Tel: {p[2]} – Propriedade: {p[3]}</li>"
    html += "</ul><br><a href='/logout'>Sair</a>"
    return html
@app.route('/painel')
def painel():
    if not session.get('logado'):
        return redirect('/login')
    return render_template('painel.html')
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
