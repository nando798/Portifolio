# lista = []

# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))

# lista = [(x, y) for x in range(3) for y in range(3)]
# print(lista)

# lista = [[letra for letra in "fernando"] for x in range(3)]

# print(lista)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_number = [numero for numero in numeros if numero > 5]

print(new_number)
