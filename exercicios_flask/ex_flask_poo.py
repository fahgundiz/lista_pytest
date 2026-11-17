# Crie uma aplicação Flask utilizando Programação Orientada a Objetos. 
# Desenvolva uma classe chamada ControllerProduto que receba uma instância da 
# aplicação Flask por meio do construtor __init__ e registre uma rota chamada 
# /produtos. Essa rota deve retornar a mensagem "Lista de produtos cadastrados". 
# Em seguida, crie uma função chamada criar_app responsável por inicializar a 
# aplicação Flask, configurar o ambiente de testes e registrar o ControllerProduto. 
# Crie um arquivo chamado test_controller.py para desenvolver testes 
# automatizados utilizando o Pytest. Implemente uma Fixture chamada app para 
# disponibilizar a aplicação configurada aos testes. Desenvolva uma função 
# chamada test_rota_produtos que utilize o método test_client() para acessar a rota 
# /produtos e verificar se o código HTTP retornado é 200 e se o conteúdo da 
# resposta corresponde à mensagem esperada. Utilize a instrução assert para 
# validar os resultados. 
from flask import Flask

def criar_app():
    app = Flask(__name__)
    app.config["TESTING"] = True

    ControllerProduto(app)

    return app

class ControllerProduto:
    def __init__(self, app):
        self.app = app

        self.registrar_rotas()
    
    def registrar_rotas(self):
        self.app.add_url_rule(
            "/produtos", "produtos", self.produtos
        )
    
    def produtos(self):
        return "Lista de produtos cadastrados"