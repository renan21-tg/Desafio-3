from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index_1.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def cntato():
    return render_template('contato.html')