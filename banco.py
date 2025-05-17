def inserir_produtor(nome, cpf, telefone, propriedade):
    conexao = sqlite3.connect('dados.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO produtores (nome, cpf, telefone, propriedade)
        VALUES (?, ?, ?, ?)
    ''', (nome, cpf, telefone, propriedade))

    conexao.commit()
    conexao.close()
