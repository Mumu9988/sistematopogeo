from flask import Flask, render_template, request, redirect, session
from banco import criar_banco, inserir_produtor, listar_produtores
import os

app = Flask(__name__)
app.secret_key = 'chave-topogeo123'  # Protege a sessão de login
criar_banco()

@app.route('/')
def home():
    return redirect('/login')

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

@app.route('/painel')
def painel():
    if not session.get('logado'):
        return redirect('/login')
    return render_template('painel.html')

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
from fpdf import FPDF
from flask import send_file

@app.route('/cadastro-projeto', methods=['GET'])
def cadastro_projeto():
    if not session.get('logado'):
        return redirect('/login')
    return render_template('cadastro_projeto.html')

@app.route('/salvar-projeto', methods=['POST'])
def salvar_projeto():
    if not session.get('logado'):
        return redirect('/login')

    nome = request.form['nome']
    valor = request.form['valor']
    objetivo = request.form['objetivo']
    linha = request.form['linha']
    produtor = request.form['produtor']

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Projeto Rural", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Nome do Projeto: {nome}", ln=True)
    pdf.cell(200, 10, txt=f"Valor: R$ {valor}", ln=True)
    pdf.multi_cell(200, 10, txt=f"Objetivo: {objetivo}")
    pdf.cell(200, 10, txt=f"Linha de Crédito: {linha}", ln=True)
    pdf.cell(200, 10, txt=f"Produtor: {produtor}", ln=True)

    caminho_pdf = "projeto_gerado.pdf"
    pdf.output(caminho_pdf)

    return send_file(caminho_pdf, as_attachment=True)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
