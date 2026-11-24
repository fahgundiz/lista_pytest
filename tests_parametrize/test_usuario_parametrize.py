# Crie uma classe chamada Usuario que receba um atributo chamado nome por 
# meio do construtor __init__. Desenvolva um método chamado validar_nome que 
# verifique se o nome informado não é None, não está vazio, não contém apenas 
# espaços em branco e possui pelo menos três caracteres. O método deverá 
# retornar True quando o nome for válido e False quando não atender às condições 
# estabelecidas. Em seguida, crie um arquivo chamado test_usuario.py para 
# desenvolver testes automatizados utilizando o Pytest. Implemente uma função 
# chamada test_validar_nome utilizando o decorator @pytest.mark.parametrize 
# para testar diferentes situações, incluindo nomes válidos, nomes muito curtos, 
# strings vazias, strings contendo apenas espaços e valores None. Utilize pelo 
# menos sete conjuntos de dados para verificar os diferentes cenários. Utilize a 
# instrução assert para validar os resultados esperados.

import pytest
from exercicios_parametrize.ex_usuario import Usuario



@pytest.mark.parametrize("nome, esperado", [
    ("gabriel", True),
    ("gabr", True),
    ("gab", True),
    ("ga", False ),
    ("", False ),
    (None, False ),
    ("      ", False ),
])
def test_validar_nome(nome, esperado):
    usuario = Usuario(nome)

    assert usuario.validar_nome() == esperado