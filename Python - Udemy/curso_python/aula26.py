"""
Formatacao basica de strings
s - string
f - float
d - int
<numero de digitos> f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,. 1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f"{variavel:=^13}")
print(f"{1000.982376128930546:0=,.2f}")
print(f"O hexadecimal de 1500 é {1500:08x}")
