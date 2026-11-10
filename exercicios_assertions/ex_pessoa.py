# Crie uma classe chamada Pessoa que possua os atributos nome e idade, 
# recebidos por meio do construtor __init__. Em seguida, crie um arquivo chamado 
# test_pessoa.py para desenvolver testes automatizados utilizando o Pytest. 
# Implemente uma função chamada test_atributos_pessoa que crie um objeto da 
# classe Pessoa com o nome "Mariana" e idade 22. Utilize a instrução assert para 
# verificar se os atributos do objeto foram inicializados corretamente.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade