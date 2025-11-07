from flask import Flask, render_template, request, redirect, url_for, flash
from models import db,Livro

app = Flask(__name__)
app.secret_key = 'chave_segura'
# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# Cria o banco de dados e as tabelas
with app.app_context():
    db.create_all()
@app.route('/')
def index():
    livros = Livro.query.all()
    return render_template('index.html', livros=livros)
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano_de_publicacao = request.form['ano_de_publicacao']
        genero = request.form['genero']
        novo_livro = Livro(titulo=titulo,autor=autor,ano_de_publicacao=ano_de_publicacao,genero=genero)
        db.session.add(novo_livro)
        db.session.commit()
        flash(f'{titulo} foi cadastrado(a) com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('cadastro.html')
if __name__ == '__main__':
    app.run(debug=True)
