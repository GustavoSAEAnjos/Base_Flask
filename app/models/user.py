from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    tipo = db.Column(db.String(20), nullable=False, default="cliente")
    nome = db.Column(db.String(100), nullable=False)

    def set_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha, senha)

    def __repr__(self):
        return f"<Usuario {self.nome}>"
