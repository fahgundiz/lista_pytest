import pytest
from exercicios_introducao.ex_multiplicacao import multiplicacao

def test_multiplicao():
    resultado = multiplicacao(6, 4)

    assert resultado == 24