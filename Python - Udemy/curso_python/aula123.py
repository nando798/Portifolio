# Escopo da classe e de métodos da clase


class Animal:
    nome = "Leao"

    def __init__(self, nome):
        self.nome = nome

    def acao(self, comer):
        return f"O {self.nome} está na floresta {comer} alimento"

    def executar(self, *args, **kwargs):
        return self.acao(*args, **kwargs)


leao = Animal(nome="Leão")
print(leao.nome)
print(leao.executar("caçando"))
