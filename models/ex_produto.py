# Crie um pequeno sistema de gerenciamento de vendas utilizando Programação
# Orientada a Objetos. Desenvolva uma classe chamada Produto, que possua os
# atributos nome e preco, e uma classe chamada Venda, que receba um objeto
# Produto e uma quantidade por meio do construtor __init__. A classe Venda deve
# conter um método chamado calcular_total que retorne o valor total da venda,
# considerando o preço do produto e a quantidade adquirida. Organize o projeto
# criando uma pasta chamada models para armazenar as classes e uma pasta
# chamada tests para armazenar os testes automatizados. Dentro da pasta tests,
# crie um arquivo chamado conftest.py para desenvolver duas Fixtures utilizando o
# decorator @pytest.fixture: uma chamada produto, responsável por criar um objeto
# da classe Produto com o nome "Monitor" e preço de R$ 900,00, e outra chamada
# venda, responsável por criar um objeto da classe Venda utilizando a Fixture
# produto como dependência e uma quantidade de 2 unidades. Crie um arquivo
# chamado test_venda.py para desenvolver testes automatizados utilizando o
# Pytest. Implemente testes para verificar os atributos do produto, a quantidade da
# venda e o resultado do método calcular_total, que deverá corresponder a R$
# 1.800,00. Utilize as Fixtures diretamente como parâmetros das funções de teste, a
# instrução assert para validar os resultados e execute os testes pelo terminal
# utilizando o comando pytest -v.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Venda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_total(self):
        return self.produto.preco * self.quantidade

    