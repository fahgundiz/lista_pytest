# Crie um programa em que contenha uma função responsável por verificar se uma 
# pessoa é maior de idade. A função deve receber a idade como parâmetro e 
# retornar True quando a idade for igual ou superior a 18 anos e False caso contrário. 
# Em seguida, crie um arquivo chamado test_idade.py para desenvolver testes 
# automatizados utilizando o Pytest. Implemente testes para verificar uma pessoa 
# com 25 anos e outra com 16 anos, utilizando a instrução assert para validar os 
# resultados esperados. 

def eh_maior_de_idade(idade):
    if idade >= 18:
        return True
    
    else:
        return False