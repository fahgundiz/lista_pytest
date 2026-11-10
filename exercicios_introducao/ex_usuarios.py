# Crie um pequeno sistema de cadastro de usuários. O programa deve 
# conter uma função responsável por verificar se um nome de usuário possui pelo 
# menos 8 caracteres. A função deve retornar True quando o nome atender ao 
# requisito e False quando possuir menos de 8 caracteres. Em seguida, crie um 
# arquivo chamado test_usuario.py para desenvolver testes automatizados 
# utilizando o Pytest. Implemente testes para verificar nomes válidos e inválidos, 
# utilize a instrução assert para validar os resultados e execute os testes pelo 
# terminal utilizando o comando pytest -v. Ao finalizar, identifique quais testes foram 
# aprovados por meio do resultado PASSED. 

def verifica_numero_caracteres(nome):
    if len(nome) >= 8:
        return True
    else:
        return False