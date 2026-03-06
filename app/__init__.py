from flask import Flask 
# Importa a classe Flask para criar a aplicação

from .models import db 
# Importa os modelos de objeto (tabelas) para criar no banco

import os 
# Importa o módulo os para acessar variáveis de ambiente

from dotenv import load_dotenv 
# Importa a função load_dotenv para carregar variáveis de ambiente de um arquivo .env
load_dotenv() 
# Carrega as variáveis de ambiente do arquivo .env para o ambiente de execução

# Função que cria o APP Flask e permite o site funcionar
def create_app():
    app = Flask(__name__)

    # Configuração do banco, pega variavel de ambiente
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    """
    Exemplo de .env:
        SECRET_KEY=super_senha_secreta
        DATABASE_URL=sqlite:///nome_do_banco.db
    """

    db.init_app(app) # Inicializa o banco de dados

    # Registrar rotas main
    from .routes import main
    app.register_blueprint(main)

    """
        Bloco exemplo para se existisse outras rotas como admin
            from .routes import adm
            app.register_blueprint(adm)
    """

    # Criar tabelas
    with app.app_context():
        db.create_all()

        # Importar modelos que vai inserir dados iniciais (Se não existir um)
        from .models.user import Usuario

        # Inserir dados iniciais se necessário
        if Usuario.query.count() == 0:
            usuario = Usuario(nome="Admin", email="admin@gmail.com", tipo="admin")
            usuario.set_senha("admin123")
            db.session.add(usuario)
            db.session.commit()

    return app # Retorna a aplicação Flask criada para ser executada no run.py