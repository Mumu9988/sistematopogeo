import sqlite3

def criar_banco():
    conn = sqlite3.connect('topogeo.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtores (
            nome TEXT,
            cpf TEXT,
            telefone TEXT,
            propriedade TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projetos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_projeto TEXT,
            valor REAL,
            objetivo TEXT,
            linha_credito TEXT,
            produtor TEXT
        )
    ''')

    conn.commit()
    conn.close()

def inserir_produtor(nome, cpf, telefone, propriedade):
    conn = sqlite3.connect('topogeo.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO produtores (nome, cpf, telefone, propriedade)
        VALUES (?, ?, ?, ?)
    ''', (nome, cpf, telefone, propriedade))
    conn.commit()
    conn.close()

def listar_produtores():
    conn = sqlite3.connect('topogeo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nome, cpf, telefone, propriedade FROM produtores")
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def inserir_projeto(nome_projeto, valor, objetivo, linha_credito, produtor):
    conn = sqlite3.connect('topogeo.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO projetos (nome_projeto, valor, objetivo, linha_credito, produtor)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome_projeto, valor, objetivo, linha_credito, produtor))
    conn.commit()
    conn.close()

def listar_projetos():
    conn = sqlite3.connect('topogeo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projetos')
    projetos = cursor.fetchall()
    conn.close()
    return projetos
