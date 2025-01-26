# Dictionary comprehension e Set comprehension

# produto = {"nome": "fernando", "idade": 39, "profissao": "Programador"}

# for chave, valor in produto.items():
#     print(chave, valor)

# dc = {
#     chave: valor.upper() if isinstance(valor, str) else valor
#     for chave, valor in produto.items()
# }


# lista = [("a", "valor a"), ("b", "valor b"), ("c", "valor c")]
# dc = {chave: valor for chave, valor in lista}


# print(dc)

s1 = {i for i in range(10)}

# print(s1)


pessoa = {"Nome:": "Neide", "Sobrenome:": "Souza"}
for chave, valor in pessoa.items():
    print(chave, valor)
