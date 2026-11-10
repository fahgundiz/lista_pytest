# Desenvolva um programa em que contenha uma função responsável por calcular 
# o preço final de um produto com desconto. A função deve receber o preço original 
# e o percentual de desconto como parâmetros e retornar o valor final da compra. 
# Crie um arquivo chamado test_desconto.py para desenvolver testes 
# automatizados utilizando o Pytest. Implemente uma função chamada 
# test_calcular_desconto que verifique se um produto de R$ 200,00 com 10% de 
# desconto apresenta o valor final de R$ 180,00. Utilize a instrução assert para 
# validar o resultado. 

def calcula_preco_final(preco_original, desconto_percentual):
    valor_final = preco_original * (1 - desconto_percentual/100)

    return valor_final


