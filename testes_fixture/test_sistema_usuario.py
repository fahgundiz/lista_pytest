# Crie um pequeno sistema de gerenciamento de usuários. Desenvolva uma classe 
# chamada Usuario que possua os atributos nome e email e uma classe chamada 
# Sistema que receba um objeto Usuario por meio do construtor __init__. A classe 
# Sistema deve conter um método chamado obter_nome_usuario que retorne o 
# nome do usuário associado ao sistema. Em seguida, crie um arquivo chamado 
# conftest.py para organizar duas Fixtures utilizando o decorator @pytest.fixture: 
# uma chamada usuario, responsável por criar um objeto da classe Usuario, e outra 
# chamada sistema, responsável por criar um objeto da classe Sistema utilizando a 
# Fixture usuario como dependência. Crie um arquivo chamado test_sistema.py 
# para desenvolver testes automatizados utilizando o Pytest. Implemente testes 
# para verificar se o sistema recebeu corretamente o usuário e se o método 
# obter_nome_usuario retorna o nome esperado. Utilize a instrução assert para 
# validar os resultados e execute os testes pelo terminal utilizando o comando 
# pytest -v. 

def test_obter_nome_usuario_retorna_nome(cria_sistema):
    sistema = cria_sistema

    assert sistema.usuario.nome == "Gabriel"

def test_obter_email_usuario_retorna_email(cria_sistema):
    sistema = cria_sistema

    assert sistema.usuario.email == "gabriel@gmail.com"