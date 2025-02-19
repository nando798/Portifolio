ano = int(input("Digite um ano: "))


if ano % 4 == 0 and ano != 0 or ano == 400:
    print(f"{ano} é um ano bisexto")
else:
    print(f"{ano} não é um ano bisexto")
