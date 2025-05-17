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
def listar_produtores():
    conexao = sqlite3.connect('dados.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, cpf, telefone, propriedade FROM produtores")
    resultados = cursor.fetchall()
    conexao.close()
    return resultados
