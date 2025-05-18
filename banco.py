import sqlite3

def criar_banco():
    conn = sqlite3.connect('topogeo.db')
    cursor = conn.cursor()

    # Tabela dos produtores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT,
            telefone TEXT,
            propriedade TEXT
        )
    ''')

    # Tabela dos projetos
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
