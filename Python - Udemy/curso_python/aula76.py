# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Fernando Souza',
#     'sobrenome': 'Pereira',
#     'idade': 40,
#     'altura': 1.74,
#     'endereços': [
#         {'avenida': 'Santo Afonso', 'número': 798},
#         {'avenida': 'Cupece', 'número': 5000},
#     ]
# }
# pessoa = dict(nome='Fernado Sozua', sobrenome='Pereira')
# print(dict(nome="Fernando", sobrenome="Souza"))


# pessoa = {
#     "nome": "fernando Souza",
#     "sobrenome": "pereira",
#     "idade": 40,
#     "altura": 1.74,
#     "enderecos": [
#         {"avenida": "Santo Afonso", "número": 798},
#         {"avenida": "Cupece", "número": 5000},
#     ],
# }

# for chave in pessoa:
#     print(chave, pessoa[chave])

# chave = "nome"
# pessoa = {}

# pessoa[chave] = "Fernandinho"
# pessoa["idade"] = 40
# pessoa["sobrenome"] = "Souza"

# # del pessoa["sobrenome"]
# print(pessoa)
# print(pessoa["nome"])

# print(pessoa.get("sobrenome", "Não existe"))

# try:
#     if pessoa.get("sobrenome") is None:
#         print("existe")
# except:
#     print(pessoa["sobrenome"])

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor, chave in pessoa.items():
#     print(valor, chave)
# import copy

# d1 = {
#     "Nome:": "Fernando",
#     "Sobrenome:": "Souza",
#     "Idade:": 40,
#     "lista": [1, 2, 3, 4, 5, 6, 7],
# }
# d2 = copy.deepcopy(d1)
# d2["lista"][3] = 887876765
# d2["Nome:"] = "Pedro"
# print(d2)
# print(d1)

# print(d1["nome:"])
# print(d1.get("nome:", "não sei o que dizer"))

# nome = d1.pop("nome:")
# print(nome)
# print(d1)
# u_chave = d1.popitem()
# print(u_chave)
# print(d1)

# d1.update({"nome:": "pinheiro", "sobrenome:": "pereira", "idade:": 45})

d1 = {"nome:": "fernando", "sobrenome:": "souza"}
tupla = (("nome:", "pedro"), ("idade:", 40))
lista = [["nome:", "pedro"], ["idade:", 40]]
d1.update(lista)
print(d1)
