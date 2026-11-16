# Pytest. Implemente testes para verificar os atributos do produto, a quantidade da
# venda e o resultado do método calcular_total, que deverá corresponder a R$
# 1.800,00. Utilize as Fixtures diretamente como parâmetros das funções de teste, a
# instrução assert para validar os resultados e execute os testes pelo terminal
# utilizando o comando pytest -v.

def test_nome_produto(venda):
    assert venda.produto.nome

def test_preco_produto(venda):
    assert venda.produto.preco == 900.00

def test_quantidade_venda(venda):
    assert venda.quantidade == 2

def preco_total_venda(venda):
    assert venda.calcular_total() == 1800