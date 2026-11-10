import pytest
from exercicios_assertions.ex_conta_bancaria import ContaBancaria

#crie um arquivo chamado test_conta.py para desenvolver testes 
# automatizados utilizando o Pytest. Implemente testes para verificar se o depósito 
# atualiza corretamente o saldo, se o saque reduz o saldo corretamente e se uma 
# tentativa de saque com valor superior ao disponível gera a exceção esperada. 
# Utilize assert e pytest.raises para realizar as verificações. 

#Cria um objeto de conta bancária
conta = ContaBancaria("Gabriel", saldo=2000)


def test_depositar_atualiza_corretamente():
    conta.depositar(500)
    #Verifica se o saldo foi alterado
    assert conta.saldo == 2500

def test_depositar_valor_zero():
    with pytest.raises(ValueError) as erro:
        conta.depositar(0)

    assert str(erro.value) == "Não é possível depositar ZERO"

def test_depositar_valor_negativo():
    with pytest.raises(ValueError) as erro:
        conta.depositar(-100)

    assert str(erro.value) == "Não é possível depositar valores negativos"

def test_sacar_funciona_com_saldo():
    #Por que foi depositado no teste de depositar 500
    conta.sacar(2500)

    assert conta.saldo == 0


#========== TESTANDO o mark.parametrize =============
@pytest.mark.parametrize("acao, valor, mensagem_erro", [
    ("sacar", 150, "Saldo insuficiente"),
    ("depositar",0, "Não é possível depositar ZERO"),
    ("depositar", -100, "Não é possível depositar valores negativos")
])
def test_multiplos_cenarios_erro(acao, valor, mensagem_erro):
    conta = ContaBancaria("Gabriel", saldo=100)

    with pytest.raises(ValueError) as erro:
        if acao == "sacar":
            conta.sacar(valor)
        elif acao == "depositar":
            conta.depositar(valor)
    
    assert str(erro.value) == mensagem_erro