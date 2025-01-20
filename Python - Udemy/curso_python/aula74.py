"""
Closure e funcoes que retornam outras funcoes
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"

    return saudar


s1 = criar_saudacao("Olá! bom dia!")
s2 = criar_saudacao("Olá! boa noite!")

print(s1("fernando"))
print(s2("neide"))
