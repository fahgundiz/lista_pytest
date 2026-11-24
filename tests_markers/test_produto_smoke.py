# Crie uma classe chamada Produto que receba os atributos nome e preco por meio
# do construtor __init__. Desenvolva métodos responsáveis por retornar o nome do
# produto, retornar seu preço e calcular um desconto de 10%. Em seguida, crie um
# arquivo chamado test_produto.py para desenvolver testes automatizados
# utilizando o Pytest. Implemente três funções de teste chamadas
# test_nome_produto, test_preco_produto e test_desconto_produto. Utilize os
# Markers personalizados smoke, integration e slow para classificar os testes de
# acordo com suas características. Registre esses Markers em um arquivo chamado
# pytest.ini, incluindo uma descrição para cada categoria. Utilize a instrução assert
# para verificar os resultados dos métodos. Execute os testes pelo terminal
# utilizando o comando pytest -v -m smoke para executar somente os testes
# classificados como smoke. Em seguida, utilize o comando pytest -v -m "smoke
# and not slow" para executar os testes smoke que não estejam classificados como
# slow.

import pytest
from exercicios_markers.ex_produto_smoke import Produto

@pytest.fixture
def produto():
    return Produto("produto", 100)

@pytest.mark.smoke
def test_nome_produto(produto):
    assert produto.retorna_nome() == "produto"

@pytest.mark.integration
def test_preco_produto(produto):
    assert produto.retorna_preco() == 100

@pytest.mark.slow
def test_desconto_produto(produto):
    assert produto.calcular_desconto(10) == 10
