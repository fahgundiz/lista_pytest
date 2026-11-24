# Crie uma classe chamada Calculadora que possua um método chamado somar, 
# responsável por receber dois valores e retornar o resultado da soma. Em seguida, 
# crie um arquivo chamado test_calculadora.py para desenvolver testes 
# automatizados utilizando o Pytest. Implemente uma função chamada test_somar 
# utilizando o decorator @pytest.mark.parametrize para testar diferentes conjuntos 
# de valores. Utilize pelo menos cinco combinações de números, verificando se o 
# resultado da soma corresponde ao valor esperado em cada situação. Utilize os 
# parâmetros valor1, valor2 e esperado para receber os dados de cada execução. 
# Utilize a instrução assert para validar os resultados. 

class Calculadora:

    def somar(self, valor1, valor2):
        return valor1 + valor2