texto = 'Fernando Souza'  # Iteráveis
indice = 0
n_nome = ""
while indice < len(texto):
    l_nome = texto[indice]
    n_nome += f"|{l_nome}"
    indice += 1

n_nome += "|"
print(n_nome) 
  




# qtd_linhas = 5
# qtd_colunas =  5

# linha = 1

# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f"{linha = }, {coluna = }")   
#         coluna += 1
#     linha += 1
    
# print("Finish")