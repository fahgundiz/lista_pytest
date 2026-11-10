import pytest
from exercicios_assertions.ex_produto import Produto

# Crie um pequeno sistema de gerenciamento de produtos utilizando Programação 
# Orientada a Objetos. Desenvolva uma classe chamada Produto que possua os 
# atributos nome, preco e quantidade. A classe deve conter um método chamado 
# calcular_total que retorne o valor total dos produtos em estoque, considerando o 
# preço e a quantidade, e um método chamado aplicar_desconto que atualize o 
# preço de acordo com o percentual informado. Desenvolva também um método 
# chamado verificar_estoque que retorne True quando houver produtos disponíveis 
# e False quando a quantidade for igual a zero. Em seguida, crie um arquivo 
# chamado test_produto.py para desenvolver testes automatizados utilizando o 
# Pytest. Implemente testes para verificar os atributos do objeto, o cálculo do valor 
# total do estoque, a aplicação de desconto e a verificação de disponibilidade de 
# produtos. Utilize a instrução assert para validar os resultados e execute os testes 
# pelo terminal utilizando o comando pytest -v.

# class Produto:
#     def __init__(self, nome, preco, quantidade):
#         self.nome = nome
#         self.preco = preco
#         self.quantidade = quantidade

#     def calcular_total(self):
#         valor_total = self.preco * self.quantidade

#         return valor_total
    
#     def aplicar_desconto(self, valor_desconto_percentual):
#         novo_preco = self.preco * (1 - valor_desconto_percentual/100)

#         self.preco = novo_preco

#     def verificar_estoque(self):
#         if self.quantidade > 0:
#             return True
#         else:
#             return False

def test_atributos_produto():
    produto = Produto("Celular", 2000, 3)

    assert produto.nome == "Celular"
    assert produto.preco == 2000
    assert produto.quantidade == 3

def test_valor_total_estoque():
    produto = Produto("Celular", 2000, 3)

    assert produto.calcular_total() == 6000

def test_valor_desconto():
    produto = Produto("Celular", 2000, 3)

    produto.aplicar_desconto(10)

    assert produto.preco == 1800

def test_disponibilidade_do_produto():
    produto = Produto("Celular", 2000, 3)

    assert produto.verificar_estoque() 