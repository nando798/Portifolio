"""Qualquer funcao ou classe em python é um objeto..."""


class Foo:
    def soma(self, x: int | float, y: int | float) -> int | float:
        """
        Soma dois números.

        :param x: Primeiro número a ser somado.
        :param y: Segundo número a ser somado.
        :return: A soma de x e y.
        """
        return x + y

    def multiplica(
        self,
        x: int | float,
        y: int | float,
        z: int | float | None = None,
    ):
        """
        Multiplica dois números.

        Multiplica x e y, e opcionalmente z se fornecido.
        :param x: Primeiro número a ser multiplicado.
        """


somar = Foo().soma
print(somar(3, 9))
# print(soma)
