import pytest

from exercicios_introducao.ex_calcular import calcula_preco_final

def test_calcular_desconto():
    valor_final = calcula_preco_final(200, 10)

    assert valor_final == 180