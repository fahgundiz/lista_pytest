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

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.quantidade * self.preco


