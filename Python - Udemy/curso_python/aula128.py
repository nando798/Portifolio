"""
Métodos de classe
São métodos onde o "Self" será "cls", ou seja,
ao invés de receber a instancia no primeiro
parâmetro, recebemos a propria classe.
"""


class Pessoa:
    ano = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("Olá, você está dentro do método de classe")

    @classmethod
    def criar_com_50(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls("Anônimo", idade)


p3 = Pessoa.criar_sem_nome(50)
p2 = Pessoa.criar_com_50("Carlos")
print(p2.nome)
print(p3.nome, p3.idade)
