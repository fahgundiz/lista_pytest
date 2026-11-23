from exercicios_parametrize.ex_produto import Produto
import pytest

@pytest.mark.parametrize("a, esperado", [
    (5, 950),
    (10, 900),
    (15, 850),
    (20, 800),
    (50, 500)
])
def test_aplicar_desconto(a, esperado):
    produto = Produto("Sucrilhos", 1000)

    assert produto.aplicar_desconto(a) == esperado