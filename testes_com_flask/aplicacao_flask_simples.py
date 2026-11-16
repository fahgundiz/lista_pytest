from flask import Flask

def criar_app():
    #Cria a aplicação
    app = Flask(__name__)

    #adiciona configurações de ambiente de teste e a chave secreta
    app.config.update(
        TESTING = True, #SELECIONA O AMBIENTE DE TESTES
        SECRET_KEY = "chave-exclusiva-de-teste"
    )

    #Cria uma rota inicial
    @app.route("/inicio")
    def inicio():
        return 'Bem-vindo ao sistema'

    return app