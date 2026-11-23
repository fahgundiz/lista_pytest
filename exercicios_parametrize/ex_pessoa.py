# Desenvolva uma classe chamada Pessoa que receba os atributos nome e idade 
# por meio do construtor __init__. Implemente um método chamado 
# maior_de_idade que verifique se a idade da pessoa é igual ou superior a 18 anos, 
# retornando True quando a condição for atendida e False caso contrário. Em 
# seguida, crie um arquivo chamado test_pessoa.py para desenvolver testes 
# automatizados utilizando o Pytest. Implemente uma função chamada 
# test_maior_de_idade utilizando o decorator @pytest.mark.parametrize para testar 
# diferentes idades, incluindo pessoas menores de idade, pessoas com exatamente 
# 18 anos e pessoas maiores de idade. Utilize pelo menos seis conjuntos de dados, 
# informando a idade e o resultado esperado em cada execução. Utilize a instrução 
# assert para verificar se o método está retornando corretamente os valores 
# booleanos.


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def maior_de_idade(self):
        return self.idade >= 18