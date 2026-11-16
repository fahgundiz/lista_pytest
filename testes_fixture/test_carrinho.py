# Crie uma classe chamada Carrinho que possua um atributo chamado produtos, 
# inicializado como uma lista vazia. A classe deve conter um método chamado 
# adicionar que permita inserir produtos na lista e um método chamado 
# quantidade_produtos que retorne a quantidade de produtos adicionados. Em 
# seguida, crie um arquivo chamado test_carrinho.py para desenvolver testes 
# automatizados utilizando o Pytest. Implemente uma Fixture chamada carrinho 
# utilizando o decorator @pytest.fixture com o escopo function, responsável por 
# criar um novo objeto da classe Carrinho para cada função de teste. Desenvolva 
# testes para adicionar produtos e verificar a quantidade de itens armazenados. 
# Utilize a instrução assert para validar os resultados e observe como cada teste 
# recebe uma nova instância do objeto. 

import pytest
from exercicios_fixture.ex_carrinho import Carrinho


@pytest.fixture
def cria_carrinho():
    return Carrinho()


#TESTE PARA VERIFICAR SE A CLASSE é da instancia carrinho
def test_instancia_carrinho(cria_carrinho):
    assert isinstance(cria_carrinho, Carrinho)

def test_adicionar_produto_carrinho(cria_carrinho):
    carrinho = cria_carrinho
    #Adicionar produto no carrinho
    carrinho.adicionar_produto("Computador", 30)
    
    #Verificar se existe um produto
    assert carrinho.quantidade_produtos() == 1

def test_carrinho_esta_vazio(cria_carrinho):
    carrinho = cria_carrinho

    assert carrinho.quantidade_produtos() == 0

def test_verificar_atributos_do_produto_no_carrinho(cria_carrinho):
    carrinho = cria_carrinho

    #Adicionar produto no carrinho
    carrinho.adicionar_produto("Computador", 30)

    #Testar o nome do produto e preço
    assert carrinho.produtos[0]["produto"] == "Computador"
    assert carrinho.produtos[0]["preco"] == 30