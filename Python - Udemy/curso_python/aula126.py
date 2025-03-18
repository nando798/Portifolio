# __dict__ e vars para atributos e instancias


class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {"nome": "Joao", "idade": 62}
p1 = Pessoa(**dados)
p1 = Pessoa("Joao", 62)
# print(f"{p1.nome} tem {p1.idade} de idade")

# p1.__dict__["outra"] = "coisa"

# print(p1.__dict__)
# print(p1.outra)
print(vars(p1))
