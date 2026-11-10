import pytest
from exercicios_assertions.ex_funcionario import Funcionario
# crie um funcionário com salário de R$ 2.000,00, aplique um aumento de 10% e 
# utilize a instrução assert para verificar se o novo salário corresponde a R$ 
# 2.200,00.

def test_aumentar_salario():
    funcionario = Funcionario("Gabriel", 2000)
    funcionario.aumentar_salario(10)

    assert funcionario.salario == 2200
