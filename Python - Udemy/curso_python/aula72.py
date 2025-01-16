# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


# def multi(*args):
#     total = 1
#     for num in args:
#         total *= num
#     return total


# multiplicacao = multi(1, 2, 3, 4, 5)
# print(multiplicacao)


# def multiply(a, b, c, d, e):
#     vezes = a * b * c * d * e
#     total = vezes
#     return total


# print(multiply(2, 3, 5, 7, 89))


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def num_par(num):
    numero = num % 2 == 0

    if numero:
        return f"{num} é Par"
    return f"{num} é Ímpar"


print(num_par(23))
print(num_par(14))
print(num_par(22))
print(num_par(57))
