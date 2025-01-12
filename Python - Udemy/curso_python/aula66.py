"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(a, b):
    print(f"{a} x {b} = {a * b}")


soma(3, 8)
soma(b=24, a=85)
