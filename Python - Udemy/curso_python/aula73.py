"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg):
    return msg


def executa(funcao):
    return funcao()


valor = executa(saudacao)
print(valor)
