import pytest

from exercicios_introducao.ex_verificar_idade import eh_maior_de_idade

def test_verificar_menor_idade():
    idade = eh_maior_de_idade(16)

    assert idade == False

def test_verificar_maior_idade():
    idade = eh_maior_de_idade(25)

    assert idade == True
    
