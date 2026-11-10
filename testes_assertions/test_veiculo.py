import pytest

# Implemente testes para verificar os atributos herdados, o 
# atributo específico da classe Carro, o funcionamento do método ligar e a relação 
# de herança utilizando a função isinstance. Utilize a instrução assert para validar os 
# resultados. 
from exercicios_assertions.ex_veiculo import Veiculo, Carro

#Cria o objeto carro para os testes
carro = Carro("Volkswagen", "golf", 4)

def test_carro_metodo_ligar():
    #Carro começa desligado, verifica se está desligado
    assert carro.ligado == False
    #Ligar o carro com o metodo
    carro.ligar()
    #Verificar se está ligado
    assert carro.ligado == True

def test_carro_eh_da_classe_carro():
    #Verifica se o carro é uma instancia da classe Carro
    assert isinstance(carro, Carro)

def test_carro_tem_marca():
    assert carro.marca == "Volkswagen"

def test_carro_tem_modelo():
    assert carro.modelo == "golf"

def test_carro_tem_portas():
    assert carro.portas == 4