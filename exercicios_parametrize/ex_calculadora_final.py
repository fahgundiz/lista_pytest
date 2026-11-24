# Crie uma classe chamada Calculadora que possua métodos responsáveis por 
# realizar as operações de soma, subtração, multiplicação e divisão. Em seguida, 
# desenvolva uma Fixture chamada calculadora utilizando o decorator 
# @pytest.fixture, responsável por disponibilizar uma instância da classe 
# Calculadora para os testes. Crie um arquivo chamado test_calculadora.py para 
# desenvolver testes automatizados utilizando o Pytest. Implemente quatro funções 
# de teste: test_somar, test_subtrair, test_multiplicar e test_dividir. Cada função 
# deverá utilizar o decorator @pytest.mark.parametrize para testar diferentes 
# conjuntos de valores, incluindo pelo menos quatro combinações para cada 
# operação. Utilize os parâmetros valor1, valor2 e esperado para representar os 
# valores utilizados em cada execução. No teste de divisão, considere diferentes 
# divisões válidas, evitando a divisão por zero. Utilize a Fixture para disponibilizar a 
# calculadora e a instrução assert para verificar os resultados de cada operação. 
# Execute os testes pelo terminal utilizando o comando pytest -v.

class Calculadora:
    
    def subtracao(self, valor_1, valor_2):
        return valor_1 - valor_2

    def adicao(self, valor_1, valor_2):
        return valor_1 + valor_2

    def multiplicacao(self, valor_1, valor_2):
        return valor_1 * valor_2

    def divisao(self, valor_1, valor_2):
        return valor_1 / valor_2