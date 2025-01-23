# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# s1 = set("Fernando")
# s1 = {"Fernando", "Souza"}
# print(s1, type(s1))

# Sets são eficientes para remover valores duplicados
# de iteraveis
# Seus valores serrão semre únicos
# não aceitam valores mutaveis
# nao te m indexes
# nao garantem ordem
# Sao iteraveis

# l1 = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 2, 2, 1, 1, 3]
# s1 = set(l1)
# print(s1)


# s1 = {1, 2, 3, 3, 3, 3, 3, 1, 2}
# for numero in s1:
#     print(numero)
# print(s1)

# s1 = set()
# # s1.add("Fernando")
# # s1.add("Neide")
# # s1.add("Dalva")
# s1.update(("Olá mundo", 1, 2, 3, 4))
# s1.clear()
# s1.discard("Fernando")
# print(s1)
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
print(s3)
s4 = s1 & s2
print(s4)
s5 = s1 - s2
print(s5)
s6 = s1 ^ s2
print(s6)
