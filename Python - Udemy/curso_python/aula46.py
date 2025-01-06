for i in range(10):
    if i == 2:
        print("vamos pular o numero 2")
        continue

    # if i == 8:
    #     print("i é 8, seu else nao existe")
    #     break

    for j in range(1,3):
        print(i, j)
else: 
    print("For compeleto com sucesso")