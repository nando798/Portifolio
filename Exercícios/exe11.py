# numero = int(input("digite um numero: "))
# divisores = 0

# for i in range(1, numero + 1):

#     if numero % i == 0:
#         divisores += 1

# if divisores == 2:
#     print("numero primo")
# else:
#     print("não é numero primo")


# numero = int(input("digite um numero: "))
# divisor = 0

# for i in range(1, numero + 1):
#     if numero % i == 0:
#         divisor += 1

# if divisor == 2:
#     print("Numero primo")
# else:
#     print("Numero não é primo")


numero = int(input("insira um numero: "))
divisor = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        divisor += 1

if divisor == 2:
    print("Numero primo")
else:
    print("Numero não é primo")
