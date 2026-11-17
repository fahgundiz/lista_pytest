# Crie uma aplicação utilizando Flask por meio de uma função chamada criar_app, 
# responsável por inicializar e retornar uma instância da classe Flask. Configure a 
# aplicação utilizando TESTING=True e defina uma SECRET_KEY exclusiva para os 
# testes. Em seguida, crie um arquivo chamado test_flask.py para desenvolver 
# testes automatizados utilizando o Pytest. Implemente uma função chamada 
# test_aplicacao_criada que verifique se a aplicação foi inicializada corretamente e 
# se a configuração TESTING está habilitada. Desenvolva também uma função 
# chamada test_chave_secreta para verificar se a chave secreta foi configurada 
# corretamente. Utilize a instrução assert para validar os resultados e execute os 
# testes pelo terminal utilizando o comando pytest -v. 
from flask import Flask

def criar_app():
    app = Flask(__name__)

    app.config.update(
        TESTING = True,
        SECRET_KEY = "chave-teste"
    )

    return app
if __name__ == "__main__":
    app = criar_app()
    app.run()