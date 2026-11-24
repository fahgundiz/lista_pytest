from exercicios_parametrize.ex_calculadora_final import Calculadora
import pytest

@pytest.fixture
def calculadora():
    return Calculadora()