# Crie uma classe chamada Veiculo que possua os atributos marca e modelo, além 
# de um método chamado ligar que retorne True quando o veículo estiver ligado e 
# False quando estiver desligado. Em seguida, crie uma classe chamada Carro que 
# herde da classe Veiculo e possua um atributo adicional chamado portas. Crie um 
# arquivo chamado test_veiculo.py para desenvolver testes automatizados 
# utilizando o Pytest. Implemente testes para verificar os atributos herdados, o 
# atributo específico da classe Carro, o funcionamento do método ligar e a relação 
# de herança utilizando a função isinstance. Utilize a instrução assert para validar os 
# resultados. 

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = not self.ligado
        return self.ligado

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas