"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

num1 = input("digite um número inteiro: ")

try:
    num1.isdigit()
    num_int = int(num1)
    par_impar = num_int % 2 == 0
    par_impar_text = 'ímpar'
    
    if par_impar:
        par_impar_text = 'par'
        
    print(f"O numero {num_int} é {par_impar_text}")
        
except:
    print("Voce nao digitou um numero inteiro!")
    
#####################################################


Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""
# entrada = input("Digite o horario: ")


# try:
#     hora = int(entrada)
    
#     if hora >= 0 and hora < 11:
#         print("Bom dia")
#     elif hora >= 12 and hora < 17:
#         print("Boa tarde")
#     elif hora >= 18 and hora < 23:
#         print("Boa Noite")
#     else:
#         print("Horário desconhecido")
# except: 
#     print("Por favor, digite apenas numeros inteiros")  
#####################################################

# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 


nome = input("Digite seu nome: ")

seu_nome = len(nome)

if seu_nome > 1:
    if seu_nome <=4:
        print("Seu nome é curto")
    elif seu_nome >=5 and seu_nome <= 6:
        print("Seu nome é normal")
    elif seu_nome > 6:
        print("Seu nome é muito grande")
else:
    print("Digite um nome válido")
    