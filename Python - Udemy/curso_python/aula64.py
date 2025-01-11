
import random

for _ in range(100):
    nove_digitos = ""
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    soma = 0
    peso = 10

    for digit in nove_digitos:
        soma += (int(digit) * peso)
        peso -= 1

    resto = (soma * 10) % 11
    resto = resto if resto <= 9 else 0

    dez_digitos = nove_digitos + str(resto)
    soma2 = 0
    peso2 = 11

    for digit in dez_digitos:
        soma2 += int(digit) * peso2
        peso2 -= 1

    resto2 = (soma2 * 10) % 11
    resto2 = resto2 if resto2 <= 9 else 0

    cpf_valido = f"{dez_digitos}{resto2}"
    print(cpf_valido)

