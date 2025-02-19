# Verifica se um numero é positivo ou negativo

numero = int(input("digite um numero valido:"))

# if numero > 0:
#     print("numero positivo")
# elif numero < 0:
#     print("Numero negativo")
# else:
#     print("numero igual a zero")

print(
    "Numero positivo"
    if numero > 0
    else "Numero negativo" if numero < 0 else "numero igual a zero"
)
