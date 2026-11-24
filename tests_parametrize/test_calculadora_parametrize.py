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
import pytest

@pytest.mark.parametrize("valor_1, valor_2, esperado", [
    (2, 2, 4),
    (-2, 2, 0),
    (10, 22, 32),
    (2, 6, 8),
])
def test_somar(calculadora, valor_1, valor_2, esperado):
    assert calculadora.adicao(valor_1, valor_2) == esperado


@pytest.mark.parametrize("valor_1, valor_2, esperado",[
    (1,2,-1),
    (6,4,2),
    (-3,-2,-1),
    (5,9,-4),
])
def test_subtrair(calculadora, valor_1, valor_2, esperado):
    assert calculadora.subtracao(valor_1, valor_2) == esperado


@pytest.mark.parametrize("valor_1, valor_2, esperado", [
    (3,2,6),
    (-2,2,-4),
    (5,-6,-30),
    (2,0,0),
])
def test_multiplicar(calculadora, valor_1, valor_2, esperado):
    assert calculadora.multiplicacao(valor_1, valor_2) == esperado

@pytest.mark.parametrize("valor_1, valor_2, esperado", [
    (2,2,1),
    (5,5,1),
    (3,2,1.5),
    (20,-4,-5),
])
def test_dividir(calculadora, valor_1, valor_2, esperado):
    assert calculadora.divisao(valor_1, valor_2) == esperado


def test_divisao_por_zero(calculadora):
    with pytest.raises(ZeroDivisionError):
        calculadora.divisao(2,0)