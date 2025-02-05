# Exercício - Adiando execução de funções
import time


def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def alguma_coisa(y):
        return funcao(x, y)

    return alguma_coisa


time.sleep(2)
soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(8))
print(multiplica_por_dez(17))
