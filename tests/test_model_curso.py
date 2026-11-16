# Desenvolva duas classes utilizando Programação Orientada a Objetos: uma
# chamada Aluno, que possua os atributos nome e nota, e outra chamada Curso,
# que possua os atributos nome e carga_horaria. Em seguida, crie um arquivo
# chamado conftest.py dentro da pasta tests para centralizar duas Fixtures
# utilizando o decorator @pytest.fixture: uma chamada aluno, responsável por criar
# um objeto da classe Aluno com o nome "Roberto" e nota 8,5, e outra chamada
# curso, responsável por criar um objeto da classe Curso com o nome "Python" e
# carga horária de 40 horas. Crie dois arquivos de teste chamados test_aluno.py e
# test_curso.py para desenvolver testes automatizados utilizando o Pytest.
# Implemente testes para verificar os atributos de cada objeto, utilize as Fixtures
# diretamente como parâmetros das funções de teste e a instrução assert para
# validar os resultados.

def test_nome_curso_correto(curso):
    assert curso.nome == "Python"

def test_carga_horaria_correta(curso):
    assert curso.carga_horaria == 40