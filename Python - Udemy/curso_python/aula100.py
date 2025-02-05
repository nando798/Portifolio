import copy
from dados import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10% - Ok
# Gere novos_produtos por deep copy (cópia profunda)


novos_produtos = [
    {**p, "preco": round(p["preco"] * 1.1, 2)} for p in copy.deepcopy(produtos)
]
print()
print("Novos produtos")
print(*novos_produtos, sep="\n")
print()


# print(novos_produtos)
# print()
# Ordene os produtos por nome decrescente (do maior para menor) - Ok
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

ordenados_por_nome = sorted(
    copy.deepcopy(produtos), key=lambda p: p["nome"], reverse=True
)
print()
print("Produtos ordenados por nome em ordem ")
print(*ordenados_por_nome, sep="\n")
print()


# Ordene os produtos por preco crescente (do menor para maior) - Ok
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p["preco"],
)

print("Produtos ordenados por preço")
print(*ordenados_por_preco, sep="\n")
