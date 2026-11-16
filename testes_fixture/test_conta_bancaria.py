# Desenvolva uma classe chamada ContaBancaria que possua os atributos titular e 
# saldo. A classe deve conter um método chamado depositar para adicionar valores 
# ao saldo e um método chamado consultar_saldo para retornar o saldo atualizado. 
# Em seguida, crie um arquivo chamado test_conta.py para desenvolver testes 
# automatizados utilizando o Pytest. Implemente uma Fixture chamada conta 
# utilizando o decorator @pytest.fixture, responsável por criar uma conta bancária 
# com titular "Mariana" e saldo inicial de R$ 500,00. Utilize a palavra-chave yield 
# para disponibilizar o objeto aos testes e exibir uma mensagem de preparação 
# antes da execução e outra de finalização após a execução. Desenvolva um teste 
# para realizar um depósito de R$ 300,00 e verificar se o saldo atualizado 
# corresponde a R$ 800,00. Utilize a instrução assert para validar o resultado e 
# execute os testes pelo terminal utilizando o comando pytest -v -s. 

import pytest
from exercicios_fixture.ex_conta_bancaria import ContaBancaria


@pytest.fixture
def conta():
    print("Preparando a conta da Mariana")
    yield ContaBancaria("Mariana", 500)
    print("Conta finalizada...")

def test_deposito(conta):
    conta.depositar(300)

    assert conta.consultar_saldo() == 800