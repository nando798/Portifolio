"""
Calculo do segundo dígito do CPF
CPF: 334.265.838-01
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  334.265.838-01 (334265838)
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

soma = 0
peso = 10
cpf = "334265838010"
cpf_9_digitos = cpf[:9]

for digit in cpf_9_digitos:
    soma = soma + (int(digit) * peso)
    peso -= 1
   

resto = soma % 11

if resto < 9:
    primeiro_digito = 0
else:
    primeiro_digito = 11 - resto

print(f"Primeiro digito verificador: ",primeiro_digito)

###########################################################

cpf = "334265838010"
cpf_10_digitos = cpf[:10]
peso_2 = 11

soma_2 = 0
for digit in cpf_10_digitos:
    soma_2 += int(digit) * peso_2
    peso_2 -= 1
 

resto = soma_2 % 11

if resto <= 9:
    segundo_digito = 0
else:
    segundo_digito = 11 - resto

print(f"Segundo digito verificador: ", segundo_digito)
