# Decoradores com parametros


def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print("fabrica_de_funcoes 1")

        def aninhada(*args, **kwargs):
            print("Parametros do decorador", a, b, c)
            print("Aninhada")
            res = func(*args, **kwargs)
            return res

        return aninhada

    return fabrica_de_funcoes


# @fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

multiplica_dez_cinco = multiplica(10, 5)
soma_dez_cinco = soma(4, 5)
print(soma_dez_cinco)
print(multiplica_dez_cinco)
