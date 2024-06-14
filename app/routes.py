from app import app
from flask import render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def cntato():
    return render_template('contato.html')

#Chave Secreta
app.secret_key = 'assessoria'

#Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'fatec'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'speccialle'

mysql = MySQL(app)

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/submit', methods = ['POST'])
def forms_enviar():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        mensagem = request.form['message']
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO Contatos (Nome, Email, Mensagem) VALUES (%s, %s, %s)', (nome, email, mensagem))
        mysql.connection.commit()
        cursor.close()
        
        flash('Mensagem enviada com sucesso!', 'success')
        return redirect(url_for('index'))
