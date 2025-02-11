def recursiva(inicio=0, fim=4):

    if inicio >= fim:
        return fim
    inicio += 1
    print(inicio, fim)

    return recursiva(inicio, fim)


print(recursiva())


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(19))
