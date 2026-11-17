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

from exercicios_flask.ex_rota import criar_app
import pytest

@pytest.fixture
def app():
    return criar_app()

def test_aplicacao_criada(app):
    assert app is not None

def test_aplicacao_testing_verdadeiro(app):
    assert app.config["TESTING"]

def test_aplicacao_chave_secreta(app):
    assert app.config["SECRET_KEY"] == "chave-teste"