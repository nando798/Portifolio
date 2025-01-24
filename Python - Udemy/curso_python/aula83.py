# Empacotamento e desempacotamento de dicionarios
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {"Nome:": "Fernando", "Sobrenome:": "Souza"}
dados_pessoa = {"Idade:": 23, "Altura:": 1.74}
pessoa_completa = {**pessoa, **dados_pessoa}

# a, b = pessoa.values()

# print(b, a)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for valor in pessoa.items():
#     print(valor)

# args e kwargs
# args = ja vimos
# kwargs = keywords arguments = argumentos nomeados


def mostra_argumentos_nomeados(*args, **kwargs):
    print("Não Nomeado", args)

    for chave, valor in kwargs.items():
        print(chave, valor)


mostra_argumentos_nomeados(Nome="Joao", Sobrenome="das Neves")
mostra_argumentos_nomeados(**pessoa_completa)

config = {
    "arg1": 1,
    "arg2": 2,
    "arg3": 3,
    "arg4": 4,
    "arg5": 5,
}

mostra_argumentos_nomeados(**config)
