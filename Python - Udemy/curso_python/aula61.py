"""
Calculo do primeiro dígito do CPF
CPF: 334.265.838-01
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  334.265.838-01 (334265838)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

soma = 0
peso = 10
cpf = "33426583801"
cpf_digitos = cpf[:9]


for digit in cpf_digitos:
    soma = soma + (int(digit) * peso)
    peso = peso - 1
    print(soma, peso)

resto = soma % 11

if resto < 2:
    primeiro_digito = 0
else:
    primeiro_digito = 11 - resto

print(f"Primeiro digito verificador: ", primeiro_digito)