"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

from itertools import zip_longest, count

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
total_lista = [x + y for x, y in zip(lista_a, lista_b)]
print(total_lista)

print("======================================")

list_total = []
for i in range(len(lista_b)):
    list_total.append(lista_a[i] + lista_b[i])
print(list_total)

print("======================================")

list_total = []
for i, _ in enumerate(lista_b):
    list_total.append(lista_a[i] + lista_b[i])
print(list_total)

print("======================================")

list_total = []
for i, _ in enumerate(lista_b):
    list_total.append(lista_a[i] + lista_b[i])
print(list_total)

print("======================================")

total_lista = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(total_lista)

print("======================================")

c1 = count(step=8, start=8)
r1 = range(2, 100, 4)

for i in r1:
    print(i)
