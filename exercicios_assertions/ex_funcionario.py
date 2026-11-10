# Desenvolva uma classe chamada Funcionario que possua os atributos nome e 
# salario. A classe deve conter um método chamado aumentar_salario que receba 
# um percentual de aumento e atualize o salário do funcionário. Em seguida, crie 
# um arquivo chamado test_funcionario.py para desenvolver testes automatizados 
# utilizando o Pytest. Implemente uma função chamada test_aumentar_salario que 
# crie um funcionário com salário de R$ 2.000,00, aplique um aumento de 10% e 
# utilize a instrução assert para verificar se o novo salário corresponde a R$ 
# 2.200,00.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aumentar_salario(self, valor_percentual_aumento):
        novo_salario = self.salario * (1 + valor_percentual_aumento/100)
        self.salario = novo_salario