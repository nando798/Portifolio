# Funcoes decoradoras e docoradores
# Decorar = Adicionar/ Remover / Restringir / Alterar
# Funcoes decoradoras sao funcoes que decoram outras funcoes
# Decoradores sao usados para fazer o Python
# usar as funcoes docoradoras em outras funcoes.


def create_function(func):
    def interna(*args, **kwargs):
        print("decoramento")
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print("Decorado")
        print(f"o resultado da decoração é: {result}")
        return result

    return interna


def inverte_nome(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError("Param deve ser uma string")


invert_check_param = create_function(inverte_nome)
invert = invert_check_param("Socorram me subi no onibus em marrocos")
print(invert)
