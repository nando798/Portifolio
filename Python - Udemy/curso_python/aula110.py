# groupby = agrupando valores (itertools)
from itertools import groupby

alunos = [
    {"nome": "luiz", "nota": "A"},
    {"nome": "leticia", "nota": "B"},
    {"nome": "fabio", "nota": "A"},
    {"nome": "rosemary", "nota": "C"},
    {"nome": "joana", "nota": "D"},
    {"nome": "joao", "nota": "A"},
    {"nome": "Eduardo", "nota": "B"},
    {"nome": "andressa", "nota": "C"},
    {"nome": "Anderson", "nota": "A"},
]


def ordena(aluno):
    return aluno["nota"]


aluno_grupos = sorted(alunos, key=ordena)

grupos = groupby(aluno_grupos, key=ordena)


for chave, grupo in grupos:
    print(chave)
    print(list(grupo))
