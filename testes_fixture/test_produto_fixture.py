# Desenvolva uma classe chamada Produto que possua os atributos nome, preco e
# quantidade. A classe deve conter um método chamado calcular_total que retorne
# o valor total dos produtos em estoque, considerando o preço e a quantidade. Em
# seguida, crie uma Fixture chamada produto utilizando o decorator @pytest.fixture,
# responsável por disponibilizar um objeto da classe Produto com o nome "Teclado",
# preço de R$ 150,00 e quantidade 5. Crie um arquivo chamado test_produto.py
# para desenvolver testes automatizados utilizando o Pytest. Implemente funções
# para verificar o nome, o preço, a quantidade e o resultado do método
# calcular_total. Utilize a Fixture como parâmetro das funções de teste e a instrução
# assert para validar os resultados.

from exercicios_fixture.ex_produto import Produto
import pytest

@pytest.fixture
def teclado():
    return Produto("Teclado", 150, 5)

def test_nome_produto(teclado):
    assert teclado.nome == "Teclado"

def test_preco_produto(teclado):
    assert teclado.preco == 150

def test_quantidade_produto(teclado):
    assert teclado.quantidade == 5

def test_valor_total_produto(teclado):
    assert teclado.calcular_total() == 5*150