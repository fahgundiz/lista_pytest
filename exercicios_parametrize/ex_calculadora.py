# Crie uma classe chamada Calculadora que possua um método chamado 
# multiplicar, responsável por receber dois valores e retornar o resultado da 
# multiplicação. Em seguida, crie um arquivo chamado test_calculadora.py para 
# desenvolver testes automatizados utilizando o Pytest. Implemente uma função 
# chamada test_multiplicar utilizando o decorator @pytest.mark.parametrize para 
# testar diferentes conjuntos de valores. Utilize pelo menos cinco combinações de 
# números, verificando se o resultado da multiplicação corresponde ao valor 
# esperado em cada situação. Utilize os parâmetros valor1, valor2 e esperado para 
# receber os dados de cada execução. Utilize a instrução assert para validar os 
# resultados e execute os testes pelo terminal utilizando o comando pytest -v. 

class Calculadora:

    def multiplicar(self, valor_1, valor_2):
        return valor_1 * valor_2
