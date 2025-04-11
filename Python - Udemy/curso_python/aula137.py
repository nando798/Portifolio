# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None


class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def adicionar_carro(self, carro):
        # Adiciona um carro a lista de motores
        carro.motor = self
        self.carros.append(carro)


class Fabricante:
    def __init__(self, fabricante):
        self.nome = fabricante
        self.carros = []

    def adicionar_carro(self, nome_carro):
        # Adiciona um carro a lista de carros do fabricante
        carro = Carro(nome_carro)
        carro.fabricante = self
        self.carros.append(carro)
        return carro


fab1 = Fabricante("Chevrolet")
motor1 = Motor("1.0 Turbo")

carro1 = fab1.adicionar_carro("Onix")
motor1.adicionar_carro(carro1)

print("Carro:", carro1.nome)
print("Motor:", carro1.motor.nome)
print("Fabricante:", carro1.fabricante.nome)

fab2 = Fabricante("Volvo")
motor2 = Motor("2.5 Hibrido")

carro2 = fab2.adicionar_carro("V90")
motor2.adicionar_carro(carro2)
print("Carro:", carro2.nome)
print("Motor:", carro2.motor.nome)
print("Fabricante:", carro2.fabricante.nome)
