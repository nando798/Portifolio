"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = tuple(enumerate(lista))
# print(lista_enumerada)
# for item in lista_enumerada:
#     print(item)

for indice, nome in enumerate(lista):
    print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print("For da Tupla: ")
#     for valor in tupla_enumerada:
#         print(f"\t{valor}")