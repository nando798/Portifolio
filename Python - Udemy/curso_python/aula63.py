"""
Calculo do segundo dígito do CPF
CPF: 472.654.010-69
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  472.654.010-69 (472654010)
   11 10  9  8  7  6  5  4  3  2
*  3   3  4  2  6  5  8  3  8  0 <-- PRIMEIRO DIGITO
   33 30 36 16 42 30 40 12  24 0

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re

soma = 0
peso = 10
cpf_usuario = re.sub(r"[^0-9]", "",
"335.627.788-05")
nove_digitos = cpf_usuario[:9]

for digit in nove_digitos:
    soma += (int(digit) * peso)
    peso -= 1

resto = (soma * 10) % 11
resto = resto if resto <= 9 else 0



soma2 = 0
peso2 = 11
dez_digitos = cpf_usuario[:10]

for digit in dez_digitos:
    soma2 += int(digit) * peso2
    peso2 -= 1

resto2 = (soma2 * 10) % 11
resto2 = resto2 if resto2 <= 9 else 0

cpf_valido = f"{nove_digitos}{resto}{resto2}"
print(cpf_valido)

if cpf_valido == cpf_usuario:
    print(f"o CPF: {cpf_valido} é valido")
else:
    print("CPF Inválido")