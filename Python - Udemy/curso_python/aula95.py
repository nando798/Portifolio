# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions


# def divide(n, d):
#     try:
#         return int(n / d)
#     except ZeroDivisionError:
#         return n

# print(divide(8, 0))


def erros_divide(d):
    if d == 0:
        raise ZeroDivisionError("Você está dividindo por zero")


def deve_ser_in_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(f"{n} deve ser int ou float", f"{tipo_n.__name__}")
    return True


def divide(n, d):
    deve_ser_in_ou_float(n)
    deve_ser_in_ou_float(d)
    erros_divide(d)

    return n / d


print(int(divide(20, "0")))
