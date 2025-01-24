# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(20)))

# lista = []
# for i in range(10):
#     lista.append(i)
# # print(lista)

# lista = [numero * 2 for numero in range(10)]
# print(lista)

# Mapeamento de dados em list comprehension
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=50)


produtos = [
    {
        "nome": "p1",
        "preco": 20,
    },
    {
        "nome": "p2",
        "preco": 10,
    },
    {
        "nome": "p3",
        "preco": 30,
    },
    # ]
    # novos_produtos = [
    #     {"nome": produto["nome"], "preço": produto["preco"]}
    #     (
    #         {**produto, "preco": produto["preco"] * 1.05}
    #         if produto["preco"] > 20
    #         else {**produto}
    #     )
    #     for produto in produtos
]
# print(*novos_produtos, sep="\n")
# p(novos_produtos)

# lista = [n for n in range(10) if n < 5]
novos_produtos = [
    # {"nome": produto["nome"], "preço": produto["preco"]}
    (
        {**produto, "preco": produto["preco"] * 1.05}
        if produto["preco"] > 20
        else {**produto}
    )
    for produto in produtos
    if produto["preco"] >= 20 and produto["preco"] > 10
]
p(novos_produtos)
