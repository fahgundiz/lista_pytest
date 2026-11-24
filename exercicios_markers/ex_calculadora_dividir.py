# Crie uma classe chamada Calculadora que possua um método chamado dividir,
# responsável por receber dois valores e retornar o resultado da divisão. Em
# seguida, crie um arquivo chamado test_calculadora.py para desenvolver testes
# automatizados utilizando o Pytest. Implemente uma função chamada test_dividir
# utilizando o decorator @pytest.mark.xfail para identificar uma situação em que o
# resultado esperado seja diferente do resultado calculado. Utilize o parâmetro
# reason para informar o motivo pelo qual a falha é esperada. Utilize os parâmetros
# valor1, valor2 e esperado para representar os valores utilizados no teste.
# Implemente também uma função de teste com o parâmetro strict=True para
# verificar o comportamento do Pytest quando um teste marcado como xfail passa
# inesperadamente. Utilize a instrução assert para validar os resultados e execute
# os testes pelo terminal utilizando o comando pytest -v -rx.

class Calculadora:
    def dividir(self, valor1, valor2):
        return valor1 / valor2