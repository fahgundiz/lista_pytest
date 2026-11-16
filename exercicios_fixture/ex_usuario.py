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


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Sistema:
    def __init__(self, usuario):
        self.usuario = usuario

    def obter_nome_usuario(self):
            return self.usuario.nome