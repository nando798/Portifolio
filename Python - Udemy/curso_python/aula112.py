# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90},
]


def filtrar_preco(produto):
    return produto["preco"] > 60


novos_produtos = [p for p in produtos if p["preco"] > 25]

new_product = filter(filtrar_preco, produtos)

produtos_ordenados = sorted(produtos, key=lambda p: p["nome"])
print("|=======Produtos=======|")
print_iter(produtos)
print()
print("|=======Novos Produtos=======|")
print_iter(novos_produtos)
print()
print("|=======Produtos Ordenados=======|")
print_iter(produtos_ordenados)
print()
print("|=======Produtos Ordenados Filter=======|")
print_iter(new_product)
