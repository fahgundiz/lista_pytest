from flask import Flask

class ControllerTeste:
    def __init__(self, app):
        self.app = app

        self.app.add_url_rule(
            "/publica", "publica", self.publica
        )

    def publica(self):
        return "Rota pública"

def criar_app():
    app = Flask(__name__)

    app.config.update(
        TESTING=True,
        SECRET_KEY = "chave-exclusiva-de-testes"
    )

    ControllerTeste(app)

    return app