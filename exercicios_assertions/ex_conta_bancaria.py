# Desenvolva uma classe chamada ContaBancaria que possua os atributos titular e 
# saldo. A classe deve conter um método chamado depositar que permita adicionar 
# valores ao saldo e um método chamado sacar que permita retirar valores da 
# conta. O método sacar deve gerar uma exceção ValueError com a mensagem 
# "Saldo insuficiente" quando o valor solicitado for maior que o saldo disponível. Em 
# seguida, crie um arquivo chamado test_conta.py para desenvolver testes 
# automatizados utilizando o Pytest. Implemente testes para verificar se o depósito 
# atualiza corretamente o saldo, se o saque reduz o saldo corretamente e se uma 
# tentativa de saque com valor superior ao disponível gera a exceção esperada. 
# Utilize assert e pytest.raises para realizar as verificações. 

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("Não é possível depositar valores negativos")
        elif valor == 0:
            raise ValueError("Não é possível depositar ZERO")
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        else:
            self.saldo -= valor