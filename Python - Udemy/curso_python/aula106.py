# Decoradores com parametros


def parametros_decorador(nome):
    def decorador(func):
        print("decorador:", nome)

        def nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f"{res} {nome}"
            return final

        return nova_funcao

    return decorador


@parametros_decorador(nome="4")
@parametros_decorador(nome="3")
@parametros_decorador(nome="2")
@parametros_decorador(nome="1")
def soma(x, y):
    return x + y


soma_dez_cinco = soma(4, 5)
print(soma_dez_cinco)
