# classes são moldes para c riar novos objetos
# As classes geream novos objetos (instancias) que
# podem ter seus proprios atributos e metodos
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar varias acoes
# por convencao, usamos PascalCase para nome das classes.

# string = "Fernando"
# print(string.upper())
# print(isinstance(string, str))


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobreome = sobrenome


p1 = Pessoa("fernando", "souza")
p2 = Pessoa("neide", "souza")
p3 = Pessoa("dalva", "martins")

print(p1.nome)
print(p1.sobreome)
print()
print(p2.nome)
print(p2.sobreome)
print()
print(p3.nome)
print(p3.sobreome)
