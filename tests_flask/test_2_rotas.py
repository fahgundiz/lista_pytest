# Desenvolva uma aplicação Flask que possua duas rotas: /inicio, responsável por 
# retornar a mensagem "Página inicial", e /sobre, responsável por retornar a 
# mensagem "Sobre o sistema". Crie uma função chamada criar_app para inicializar 
# a aplicação e registrar as duas rotas. Em seguida, organize o projeto criando uma 
# pasta chamada tests e um arquivo chamado conftest.py para desenvolver uma 
# Fixture chamada app utilizando o decorator @pytest.fixture. A Fixture deve criar a 
# aplicação Flask, habilitar a configuração TESTING=True e disponibilizar a instância 
# para diferentes arquivos de teste. Crie um arquivo chamado test_rotas.py para 
# desenvolver testes automatizados utilizando o Pytest. Implemente testes para 
# verificar o acesso às duas rotas, os códigos HTTP retornados e as mensagens 
# apresentadas em cada resposta. Utilize o método test_client() e a instrução assert 
# para validar os resultados. Execute os testes pelo terminal utilizando o comando 
# pytest -v. 

def test_rota_inicio_devolve_200(app):
    with app.test_client() as client:
        resposta = client.get('/inicio')

    assert resposta.status_code == 200

def test_rota_sobre_devolve_200(app):
    with app.test_client() as client:
        resposta = client.get("/sobre")
    
    assert resposta.status_code == 200

def test_rota_inicio_devolve_msg(app):
    with app.test_client() as client:
        resposta = client.get("/inicio")

    assert resposta.get_data(as_text=True) == "Página inicial"

def test_rota_sobre_devolve_msg(app):
    with app.test_client() as client:
        resposta = client.get("/sobre")

    assert resposta.get_data(as_text=True) == "Sobre o sistema"