import pytest
from exercicios_introducao.ex_subtracao import subtracao


def test_subtracao():
    resultado = subtracao(15, 5)

    assert resultado == 10

#========= PARA TESTAR =========
#python -m pytest -v