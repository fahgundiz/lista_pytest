import pytest
from exercicios_assertions.ex_pessoa import Pessoa
# Implemente uma função chamada test_atributos_pessoa que crie um objeto da 
# classe Pessoa com o nome "Mariana" e idade 22. Utilize a instrução assert para 
# verificar se os atributos do objeto foram inicializados corretamente.

def test_atributos_pessoa():
    pessoa = Pessoa("Mariana", 22)

    assert pessoa.nome == "Mariana"
    assert pessoa.idade == 22