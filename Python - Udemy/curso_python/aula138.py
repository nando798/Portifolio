# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class


class Pessoa:

    cpf = "123.456.789-10"

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print("Segundo - classe pessoa, a penultima na ordem de heranca")
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print("Primeiro - aqui estamos na classe Cliente, vem antes da classe Pessoa")
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    pass


c1 = Cliente("Fernando", "Pereira")
c1.falar_nome_classe()

a1 = Aluno("Maria", "Silva")
a1.falar_nome_classe()
print(a1.cpf)
