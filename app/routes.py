from flask import Blueprint, request, render_template, redirect, url_for # Importa o Flask e suas coisas para funcionar
from .models.user import Usuario # Importa a tabela de usuarios
from . import db

main = Blueprint("main", __name__) # Define o Blueprint para as rotas principais do aplicativo

@main.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        usuario = Usuario(
            nome=nome,
            email=email
        )

        usuario.set_senha(senha)

        db.session.add(usuario)
        db.session.commit()

        return redirect(url_for("main.home"))

    usuarios = Usuario.query.all()

    return render_template(
        "index.html",
        usuarios=usuarios
    )

@main.route("/exemplo_rota")
def exemplo_rota():
    return render_template("exemplo_rota.html") # Rota de exemplo para mostrar como criar uma rota simples


"""
    Exemplo de rota usando o Blueprint de adm considerando que está em uma pasta chamada adm:
    Automaticamente coloca o prefixo da pasta na url
    adm = Blueprint("adm", __name__, url_prefix="/adm")

    @adm.route("/admin")
    def admin():
        return render_template("adm/index.html")
"""
