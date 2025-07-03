"""Qualquer funcao ou classe em python é um objeto..."""


def soma(x: int | float, y: int | float) -> int | float:
    """
    Soma dois números.

    :param x: Primeiro número a ser somado.
    :param y: Segundo número a ser somado.
    :return: A soma de x e y.
    """
    return x + y


def multiplica(
    x: int | float,
    y: int | float,
    z: int | float | None = None,
):
    """
    Multiplica dois números.

    Multiplica x e y, e opcionalmente z se fornecido.
    :param x: Primeiro número a ser multiplicado.
    """


soma(3.9, 4.2)

print(soma.__doc__)
# print(soma)
print(multiplica.__doc__)
