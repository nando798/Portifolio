# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


# def nomes_cidades(l1, l2):
#     intervalo = min(len(cidade), len(estado))
#     return [(l1[i], l2[i]) for i in range(intervalo)]


# print(nomes_cidades(cidade, estado))
from itertools import zip_longest

cidade = ["Salvador", "Ubatuba", "Belo Horizonte"]
estado = ["BA", "SP", "MG", "RJ"]

for i, j in zip(cidade, estado):
    print(i, j)

print(list(zip(cidade, estado)))
print(list(zip_longest(cidade, estado, fillvalue="Sem cidade")))
