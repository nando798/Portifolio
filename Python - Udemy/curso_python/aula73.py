"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f"{msg} | O palestrante será o {nome}"


def executa(funcao, *args):
    return funcao(*args)


valor = executa(saudacao, "Ola a todos, tenham uma ótima noite", "Fernando")
print(valor)
