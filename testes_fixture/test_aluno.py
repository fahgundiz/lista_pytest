# Crie uma classe chamada Aluno que possua os atributos nome, idade e curso,
# recebidos por meio do construtor __init__. Em seguida, crie um arquivo chamado
# test_aluno.py para desenvolver testes automatizados utilizando o Pytest.
# Implemente uma Fixture chamada aluno utilizando o decorator @pytest.fixture,
# responsável por criar um objeto da classe Aluno com o nome "Lucas", idade 21 e
# curso "Análise e Desenvolvimento de Sistemas". Desenvolva funções de teste para
# verificar se os atributos do objeto foram inicializados corretamente. Utilize a
# instrução assert para validar os resultados e evite criar o mesmo objeto
# manualmente dentro de cada teste

import pytest

@pytest.fixture
def aluno():
    from exercicios_fixture.ex_aluno import Aluno

    return Aluno("Lucas", 21, "Análise e Desenvolvimento de Sistemas")

def test_nome_aluno_correto(aluno):
    assert aluno.nome == "Lucas"

def test_idade_aluno_correta(aluno):
    assert aluno.idade == 21

def test_curso_aluno_correta(aluno):
    assert aluno.curso == "Análise e Desenvolvimento de Sistemas"