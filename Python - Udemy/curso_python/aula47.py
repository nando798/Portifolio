"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
palavra_secreta = "mariane"
lista_progresso = ['*'] * len(palavra_secreta)
tentativas = 0

while '*' in lista_progresso:
    print("progresso: ", "".join(lista_progresso))
    
    letra = input("digite uma letra da palavra secreta: ")

    if not letra.isalpha() or len(letra) > 1:
        print("Digite apenas uma letra: ")
        continue

    tentativas += 1
      
    
    for i in range(len(palavra_secreta.lower())):
        if palavra_secreta[i] in palavra_secreta:
            if palavra_secreta[i].lower() == letra.lower():
                lista_progresso[i] = palavra_secreta[i]

            os.system("cls") 
    
print("PARABENS, VOCÊ ACERTOU A PALAVRA - ",palavra_secreta)    

print ("Numero de tentativas: ", tentativas)




    