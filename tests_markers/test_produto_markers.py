# Crie uma classe chamada Produto que receba os atributos nome e preco por meio 
# do construtor __init__. Desenvolva um método chamado calcular_preco que 
# retorne o preço do produto. Em seguida, crie um arquivo chamado test_produto.py 
# para desenvolver testes automatizados utilizando o Pytest. Implemente uma 
# função chamada test_calcular_preco utilizando o decorator @pytest.mark.skip 
# para ignorar temporariamente a execução do teste, informando o motivo por meio 
# do parâmetro reason. Crie também uma função chamada test_nome_produto 
# para verificar se o nome do produto está sendo armazenado corretamente. Utilize 
# a instrução assert para validar os resultados. Execute os testes pelo terminal 
# utilizando o comando pytest -v -rs e observe como o Pytest apresenta os testes 
# ignorados e seus respectivos motivos. 

import pytest
from exercicios_markers.ex_produto import Produto

@pytest.mark.skip(reason="Ainda desenvolvendo o teste")
def test_calcular_preco():
    pass

@pytest.mark.parametrize("nome, esperado", [
    ("gabriel", "gabriel"),
    ("leonardo", "leonardo"),
    ("Roberto", "Roberto")
])
def test_nome_produto(nome, esperado):
    assert Produto(nome,30).nome == esperado