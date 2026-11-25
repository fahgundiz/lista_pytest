# Crie uma classe chamada Usuario que receba os atributos nome e email por meio
# do construtor __init__. Desenvolva métodos responsáveis por validar o nome e
# verificar se o email contém o caractere @. Em seguida, crie um arquivo chamado
# test_usuario.py para desenvolver testes automatizados utilizando o Pytest.
# Implemente uma classe de testes chamada TestUsuario e aplique o Marker
# personalizado @pytest.mark.smoke diretamente sobre ela, classificando todos os
# seus métodos como testes essenciais. Implemente as funções test_validar_nome
# e test_validar_email, utilizando a instrução assert para verificar os resultados
# esperados. Adicione também o Marker @pytest.mark.slow em um dos métodos de
# teste. Registre os Markers no arquivo pytest.ini. Execute os testes pelo terminal
# utilizando o comando pytest -v -m "smoke and not slow" e observe como o Pytest
# seleciona os testes de acordo com as classificações aplicadas.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def validar_email(self):
        if "@" not in self.email:
            return False

        return True

    def validar_nome(self):
        if len(self.nome) < 3:
            return False

        return True