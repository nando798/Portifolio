valor = "subi no pe de lima"

i =0

while i < len(valor):
    letra = valor[i]
    nome = letra
    i += 1
    
    print(letra)
    
    if letra == " ":
        break
else:
    print("Não era pra ter chego nesse ponto")
    
print("fim do app")