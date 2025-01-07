"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

# #            +01234
# #            -54321

# string = "ABCDE"
# lista = [123, 456, "fernando", True, []]
# print(lista , type(lista))
# lista[2] = "casa da maria joana"
# print(lista[2], type(lista[2]))

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# numeros = [10,20,30,40,50,60,70]
# numeros.pop(2)

# numeros.append(80)
# numeros.append("Fernando")
# nome = numeros.pop()
# numeros.insert(4, 5)
# print(numeros, nome)

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)

nome = "fernando"
outro_nome = nome
nome = "Joao"
print(nome)
print(outro_nome)

lista_a =["Fernando", "Silvina", 1, 2.8]
lista_b = lista_a.copy()

lista_a[0] = "Dalva e Neide"

print(lista_b)
print(lista_a)