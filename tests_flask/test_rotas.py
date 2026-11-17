# Desenvolva uma aplicação Flask que possua uma rota chamada /inicio, 
# responsável por retornar a mensagem "Bem-vindo ao sistema". Utilize uma função 
# chamada criar_app para inicializar a aplicação e registrar a rota. Em seguida, crie 
# um arquivo chamado test_rotas.py para desenvolver testes automatizados 
# utilizando o Pytest. Implemente uma Fixture chamada app utilizando o decorator 
# @pytest.fixture, responsável por criar e configurar a aplicação com TESTING=True. 
# Desenvolva uma função de teste que utilize o recurso test_client() do Flask para 
# acessar a rota /inicio e verificar se a resposta apresenta o código HTTP 200 e a 
# mensagem esperada. Utilize a instrução assert para validar os resultados sem 
# precisar iniciar manualmente o servidor Flask. 

import pytest
from exercicios_flask.ex_rota_inicio import criar_app


@pytest.fixture
def client():
    app = criar_app()

    app.config.update(
        TESTING = True
    )

    with app.test_client() as client:
        yield client #yields substitui o return


def test_rota_inicio_retorna_codigo_200(client):
    resposta = client.get('/inicio')

    assert resposta.status_code == 200

def test_rota_inicio_retorna_msg(client):
    #app -> utiliza o método test_client() que utiliza o metodo get('/nome_rota')
    resposta = client.get('/inicio')

    assert resposta.get_data(as_text= True) == "Bem-vindo ao sistema"

