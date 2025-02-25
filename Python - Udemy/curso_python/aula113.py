# reduce - faz a reducao de um iteravel em um valor
from functools import reduce

produtos = [
    {"nome": "Produto 5", "preco": 10},
    {"nome": "Produto 1", "preco": 22},
    {"nome": "Produto 3", "preco": 10},
    {"nome": "Produto 2", "preco": 105},
    {"nome": "Produto 4", "preco": 69},
]


# def funcao_reduce(acumulador, produto):
#     print("acumulador", acumulador)
#     print("produto", produto)
#     print()
#     return acumulador + produto["preco"]


total = reduce(lambda ac, p: ac + p["preco"], produtos, 0)

print("o total é: ", total)
# total = ""
# total = 0
# for p in produtos:
#     total += p["preco"]
# print(total)

# print(sum(p["preco"] for p in produtos))
