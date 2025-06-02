# Classes decoradoras (Decorator classes)


class Multiplicar:
    def __init__(self, multiplicador):
        self.multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multiplicador

        return interna


@Multiplicar(2)
def soma(a, b):
    return a + b


somar = soma(2, 6.3)
print(somar)
