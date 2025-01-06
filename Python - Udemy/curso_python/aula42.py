frase = "O python é uma linguagem de programação multiplataforma criada por Guido Van Rossum. "

i = 0
quantas_vezes_apareceu = 0
letras_apareceu_mais_vezes = ""

while i < len(frase):
    frase_atual = frase[i]
    
    if frase_atual == " ":
        i += 1
        continue
    
    quantas_vezes_apareceu_atual = frase.count(frase_atual)
    
    if quantas_vezes_apareceu <= quantas_vezes_apareceu_atual:
        quantas_vezes_apareceu = quantas_vezes_apareceu_atual
        letras_apareceu_mais_vezes = frase_atual
        
    i += 1
    
print(f"A letra que apareceu mais foi: '{letras_apareceu_mais_vezes}', apareceu: {quantas_vezes_apareceu}x")     
    
    
