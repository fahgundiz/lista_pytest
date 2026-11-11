# Crie uma classe chamada Aluno que possua os atributos nome, idade e curso,
# recebidos por meio do construtor __init__. Em seguida, crie um arquivo chamado
# test_aluno.py para desenvolver testes automatizados utilizando o Pytest.
# Implemente uma Fixture chamada aluno utilizando o decorator @pytest.fixture,
# responsável por criar um objeto da classe Aluno com o nome "Lucas", idade 21 e
# curso "Análise e Desenvolvimento de Sistemas". Desenvolva funções de teste para
# verificar se os atributos do objeto foram inicializados corretamente. Utilize a
# instrução assert para validar os resultados e evite criar o mesmo objeto
# manualmente dentro de cada teste

class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso


