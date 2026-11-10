import pytest
from exercicios_introducao.ex_usuarios import verifica_numero_caracteres

def test_nome_valido():
    resultado = verifica_numero_caracteres("Gabriela")

    assert resultado == True

def test_nome_invalido():
    resultado = verifica_numero_caracteres("jão")

    assert resultado == False