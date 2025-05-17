import sqlite3

def criar_banco():
    from flask import Flask, render_template, request
from banco import inserir_produtor  # importa a função que salva no banco

app = Flask(__name__)

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
    
    inserir_produtor(nome, cpf, telefone, propriedade)  # chama a função do banco
    return f"Produtor {nome} cadastrado com sucesso!"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

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
