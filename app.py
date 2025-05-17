import sqlite3

def criar_banco():
    conexao = sqlite3.connect('dados.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT,
            propriedade TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

def inserir_produtor(nome, cpf, telefone, propriedade):
    conexao = sqlite3.connect('dados.db')
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO produtores (nome, cpf, telefone, propriedade)
        VALUES (?, ?, ?, ?)
    ''', (nome, cpf, telefone, propriedade))
    conexao.commit()
    conexao.close()
from flask import Flask, render_template, request
from banco import inserir_produtor, listar_produtores, criar_banco
import os

app = Flask(__name__)
criar_banco()  # cria o banco ao iniciar

@app.route('/')
def home():
    return "Sistema Topogeo rodando!"

@app.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    telefone = request.form['telefone']
    propriedade = request.form['propriedade']
    
    inserir_produtor(nome, cpf, telefone, propriedade)
    return f"Produtor {nome} cadastrado com sucesso!"

@app.route('/listar')
def listar():
    produtores = listar_produtores()
    html = "<h1>Produtores Cadastrados</h1><ul>"
    for p in produtores:
        html += f"<li>{p[0]} – CPF: {p[1]} – Tel: {p[2]} – Propriedade: {p[3]}</li>"
    html += "</ul>"
    return html

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
