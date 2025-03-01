# Entendendo o self classes Python
# Classes - Moldes (Geralmente sem dados)
# Instancias da classe (objetos - Tem os dados)
# Uma classe pode gerar varias instancias.
# Na classe o self é a propria instancia.


class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self, velocidade):
        print(f"{self.nome} acelerou a {velocidade} km/h")

    def marca(self, marca):
        print(f"{self.nome} é da marca {marca}")


carro = Carro("fusca")
carro.acelerar(120)
carro.marca("volkswagen")

gol = Carro("gol")
Carro.acelerar(gol, 100)
