# Funcoes decoradoras e docoradores
# Decorar = Adicionar/ Remover / Restringir / Alterar
# Funcoes decoradoras sao funcoes que decoram outras funcoes
# Decoradores sao usados para fazer o Python
# usar as funcoes docoradoras em outras funcoes.
# Decoradores são "Syntax Suggar" (Açucar Sintático)


def create_function(func):
    def interna(*args, **kwargs):
        print("vou decorar suas funçãoes!")
        print()
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print("Funções decoradas com sucesso!")
        print()
        print(f"o resultado da decoração é: {result}")
        print()

        return result

    return interna


@create_function
def invert_name(string):
    print(f"{invert_name.__name__}")
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError("Param deve ser uma string")


invert = invert_name("Socorram me subi no onibus em marrocos")
# print(invert)
