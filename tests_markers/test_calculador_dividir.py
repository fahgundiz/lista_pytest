# Crie uma classe chamada Calculadora que possua um método chamado dividir,
# responsável por receber dois valores e retornar o resultado da divisão. Em
# seguida, crie um arquivo chamado test_calculadora.py para desenvolver testes
# automatizados utilizando o Pytest. Implemente uma função chamada test_dividir
# utilizando o decorator @pytest.mark.xfail para identificar uma situação em que o
# resultado esperado seja diferente do resultado calculado. Utilize o parâmetro
# reason para informar o motivo pelo qual a falha é esperada. Utilize os parâmetros
# valor1, valor2 e esperado para representar os valores utilizados no teste.
# Implemente também uma função de teste com o parâmetro strict=True para
# verificar o comportamento do Pytest quando um teste marcado como xfail passa
# inesperadamente. Utilize a instrução assert para validar os resultados e execute
# os testes pelo terminal utilizando o comando pytest -v -rx.

import pytest
from exercicios_markers.ex_calculadora_dividir import Calculadora

@pytest.mark.xfail(reason="Erro esperado na divisão vai passar com XFAIL")
@pytest.mark.parametrize("valor1, valor2, esperado", [
    (10,2,100)
])
def test_calculadora_dividir(valor1, valor2, esperado):
    assert Calculadora().dividir(valor1, valor2) == esperado

@pytest.mark.xfail(reason="Teste marcado com xfail, mas a lógica do assert está corrigida e vai passar com XPASS")
def test_calculadora_dividir_xpass():
    assert Calculadora().dividir(10,2) == 5


@pytest.mark.xfail(
        reason= "teste marcado com xfail, mesmo corrigido não vai passar pois possui o strict = True", 
        strict=True)
def test_calculadora_dividir_strict_true():
    assert Calculadora().dividir(10,2) == 5