# Crie uma classe chamada Cliente que possua os atributos nome, email e idade,
# recebidos por meio do construtor __init__. Em seguida, organize o projeto criando
# uma pasta chamada models para armazenar a classe e uma pasta chamada tests
# para armazenar os arquivos de teste. Dentro da pasta tests, crie um arquivo
# chamado conftest.py para desenvolver uma Fixture chamada cliente utilizando o
# decorator @pytest.fixture, responsável por criar um objeto da classe Cliente com
# o nome "Fernanda", email "fernanda@email.com" e idade 25. Crie um arquivo
# chamado test_cliente.py para desenvolver testes automatizados utilizando o
# Pytest. Implemente funções para verificar se os atributos do objeto foram
# inicializados corretamente. Utilize a Fixture diretamente como parâmetro das
# funções de teste e a instrução assert para validar os resultados, sem realizar
# importações manuais da Fixture.

def test_cliente_nome_correto(cliente):
    assert cliente.nome == "Fernanda"

def test_cliente_email_correto(cliente):
    assert cliente.email == "fernanda@email.com"

def test_cliente_idade_correta(cliente):
    assert cliente.idade == 25