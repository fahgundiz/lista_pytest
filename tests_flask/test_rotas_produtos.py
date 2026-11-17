# Implemente uma Fixture chamada app para 
# disponibilizar a aplicação configurada aos testes. Desenvolva uma função 
# chamada test_rota_produtos que utilize o método test_client() para acessar a rota 
# /produtos e verificar se o código HTTP retornado é 200 e se o conteúdo da 
# resposta corresponde à mensagem esperada. Utilize a instrução assert para 
# validar os resultados. 

from exercicios_flask.ex_flask_poo import criar_app
import pytest

@pytest.fixture
def app():
    return criar_app()

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

def test_rota_produtos_devolve_status_200(client):
    resposta = client.get("/produtos")

    assert resposta.status_code == 200

def test_rota_produtos_devolve_msg_correta(client):
    resposta = client.get("/produtos")

    assert resposta.get_data(as_text = True) == "Lista de produtos cadastrados"