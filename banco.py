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
    import sqlite3

def criar_banco():
    conn = sqlite3.connect('topogeo.db')
    cursor = conn.cursor()

    # Tabela dos produtores (já tinha)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtores (
            nome TEXT,
            cpf TEXT,
            telefone TEXT,
            propriedade TEXT
        )
    ''')

    # NOVO: Tabela dos projetos
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
