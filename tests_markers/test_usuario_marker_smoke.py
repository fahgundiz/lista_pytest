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

import pytest
from exercicios_markers.ex_usuario_marker import Usuario

@pytest.fixture
def usuario():
    return Usuario("Gabriel","gabriel@hotmail.com")

@pytest.mark.smoke
class TestUsuario:
    def test_validar_nome(self, usuario):
        assert usuario.validar_nome()

    @pytest.mark.slow
    def test_validar_email(self, usuario):
        assert usuario.validar_email()