# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO = "aula127.json"


class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa("Joao", 62)
p2 = Pessoa("Fernando", 37)
p3 = Pessoa("Neide", 32)
bd = [p1.__dict__, vars(p2), p3.__dict__]


def fazendo_dump():
    with open(CAMINHO, "w") as arquivo:
        json.dump(bd, arquivo, indent=4)

    print("Dados salvo em arquivo.json")
