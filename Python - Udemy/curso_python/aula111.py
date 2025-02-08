# map = para mapear dados
from functools import partial


def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


produtos = [
    {"nome": "prod 5", "preco": 10.00},
    {"nome": "prod 1", "preco": 22.32},
    {"nome": "prod 5", "preco": 10.11},
    {"nome": "prod 5", "preco": 105.87},
    {"nome": "prod 5", "preco": 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)


def aumentar_preco_produto(produto):
    return {**produto, "preco": aumentar_dez_porcento(produto["preco"])}


novos_produtos = map(aumentar_preco_produto, produtos)

# novos_produtos = [{**p, "preco": aumentar_dez_porcento(p["preco"])} for p in produtos]


print(list(map(lambda x: x * 3, [1, 2, 3, 4, 5, 6])))


# print_iter(novos_produtos)
# print_iter(produtos)


# def aumentar_porcentagem(valor, porcentagem):
#     return round(valor * porcentagem)


# aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)


# novos_produtos = [{**p, "preco": aumentar_dez_porcento(p["preco"])} for p in produtos]


# def aumentar_preco_produto(produto):
#     return {**produto, "preco": aumentar_dez_porcento(produto["preco"])}


# novos_produtos = map(aumentar_preco_produto, produtos)


# print_iter(novos_produtos)
# print_iter(produtos)
