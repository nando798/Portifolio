#Operadores in e in not
#strings sao iteráveis
nome = 'Fernando'
# print(nome[3]) 

# print(20 *"=")

# print("nando" in nome)
# print("nando" not in nome)

encontrar = input("Digite o caractere que deseja encontrar:")

if encontrar in nome:
    print(f"o caractere {encontrar} está em {nome}")
else:
    print(f"o caractere {encontrar} não está em {nome}")



