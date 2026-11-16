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

class Carrinho:
    def __init__(self):
        self.produtos = []

    
    def quantidade_produtos(self):
        return len(self.produtos)
    
    def adicionar_produto(self, produto, preco):
        self.produtos.append({
            "produto" : produto,
            "preco" : preco
        })
