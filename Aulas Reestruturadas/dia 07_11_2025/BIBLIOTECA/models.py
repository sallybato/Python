from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Livro(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    titulo = db.Column(db.String(100), unique= True, nullable=False)
    autor = db.Column(db.String(100),  nullable=False)
    ano_de_publicacao = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f'<Livro{self.titulo}>'
