# Crie uma classe chamada Usuario que receba os atributos nome e idade por meio
# do construtor __init__. Desenvolva um método chamado maior_de_idade que
# retorne True quando a idade for igual ou superior a 18 anos e False caso contrário.
# Em seguida, crie um arquivo chamado test_usuario.py para desenvolver testes
# automatizados utilizando o Pytest. Implemente uma função chamada
# test_maior_de_idade utilizando o decorator @pytest.mark.skipif para ignorar a
# execução do teste quando a versão do Python for inferior à 3.10. Utilize o módulo
# sys e o atributo sys.version_info para verificar a versão instalada. Informe o motivo
# da condição utilizando o parâmetro reason. Utilize a instrução assert para verificar
# se o método está retornando corretamente os valores booleanos.

class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def maior_de_idade(self):
        return self.idade >= 18