# Desenvolva uma classe chamada Estoque que possua os atributos produto e
# quantidade. A classe deve conter um método chamado adicionar_estoque que
# permita aumentar a quantidade de produtos e um método chamado
# consultar_quantidade que retorne a quantidade disponível. Em seguida, crie um
# arquivo chamado conftest.py dentro da pasta tests para desenvolver uma Fixture
# chamada estoque utilizando o decorator @pytest.fixture com o escopo module,
# responsável por criar um objeto da classe Estoque com o produto "Mouse" e
# quantidade inicial de 10 unidades. Crie um arquivo chamado test_estoque.py para
# desenvolver testes automatizados utilizando o Pytest. Implemente funções para
# verificar o produto cadastrado, a quantidade inicial e o funcionamento do método
# adicionar_estoque. Utilize a Fixture diretamente como parâmetro das funções de
# teste e a instrução assert para validar os resultados. Observe como os testes
# compartilham a mesma instância do objeto durante a execução do módulo e
# considere as alterações realizadas no estoque ao elaborar as verificações.

class Estoque:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade_adicionada):
        if quantidade_adicionada <= 0 or not isinstance(quantidade_adicionada, int):
            raise ValueError("Insira um quantidade inteira positiva")
        self.quantidade += quantidade_adicionada

    