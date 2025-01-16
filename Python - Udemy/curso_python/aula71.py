"""
args - Argumentos não nomeados
* - * aargs (empacotamento e desempacotamento)
lembre-te de desempacotamento
"""

# x, y, *resto = 1, 2, 3, 4, 5
# print(x, y, resto)

# def soma(x,y):
#     return soma


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


numero = 1, 2, 3, 4, 5, 6, 7
# soma_ = soma(1, 2, 3, 4, 5, 6, 7)


print(sum(numero))
