@app.route('/projeto', methods=['GET', 'POST'])
def projeto():
    if not session.get('logado'):
        return redirect('/login')
    
    if request.method == 'POST':
        nome_projeto = request.form['nome_projeto']
        valor = request.form['valor']
        objetivo = request.form['objetivo']
        linha = request.form['linha']
        produtor = request.form['produtor']
        
        # Aqui depois a gente gera o PDF com essas infos
        return f"Projeto '{nome_projeto}' cadastrado com sucesso! (PDF será gerado em breve)"

    return render_template('projeto.html')
