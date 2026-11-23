# Crie uma classe chamada Produto que receba os atributos nome e preco por meio 
# do construtor __init__. Desenvolva um método chamado aplicar_desconto que 
# receba um percentual e retorne o preço do produto após a aplicação do desconto. 
# Em seguida, crie um arquivo chamado test_produto.py para desenvolver testes 
# automatizados utilizando o Pytest. Implemente uma função chamada 
# test_aplicar_desconto utilizando o decorator @pytest.mark.parametrize para 
# testar diferentes percentuais de desconto, como 5%, 10%, 15%, 20% e 50%. 
# Utilize um produto com preço inicial de R$ 1.000,00 e informe o resultado 
# esperado para cada percentual. Utilize os parâmetros percentual e esperado para 
# receber os valores de cada execução. Utilize a instrução assert para verificar se o 
# método está calculando corretamente os descontos aplicados.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco = self.preco * (1-percentual/100)
        return self.preco