import os

# Criando arquivos com Python + Context Manager with
# Usamos a funÃ§Ã£o open para abrir
# um arquivo em Python (ele pode ou nÃ£o existir)
# Modos:
# r (leitura), w (escrita), x (para criaÃ§Ã£o)
# a (escreve ao final), b (binÃ¡rio)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# MÃ©todos Ãºteis
# write, read (escrever e ler)
# writelines (escrever vÃ¡rias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o mÃ³dulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o mÃ³dulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# caminho_arquivo = r"C:\\Users\\nando\\Documents\\"
# caminho_arquivo += "aula116.txt"

# # caminho_total = open(caminho_arquivo, "w")
# # caminho_total.close()

# with open(caminho_arquivo, "w") as arquivo:
#     print(type(arquivo))
#     arquivo.write(
#         "posso nao ter muito conhecimento em programacao agora, mas no futuro serei um otimo profisssional com a fÃ© em Deus!\r\n"
#     )
#     arquivo.writelines(
#         (
#             "subi no pe de lima\n",
#             "para ver o meu amor passar\n",
#             "ele nao passou\n",
#             "eu desci\n",
#         )
#     )
#     arquivo.seek(0, 0)
#     arquivo.write("Quero estudar pra dar um melhor futuro pra minha familia!\r\n")

# with open(caminho_arquivo, "r") as arquivo:
#     print(arquivo.read())


caminho_arquivo = r"C:\\Users\\nando\\Documents\\"
caminho_arquivo += "aula116.txt"

caminho_total = open(caminho_arquivo, "w")
caminho_total.close()

with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("arquivo paginado do coração puro\n")
    arquivo.write("arquivo paginado do coração puro | versao 2.0\n")
    arquivo.writelines(("arquivo de paginação orientado a objeto"))
print(caminho_total)

os.rename(caminho_arquivo, "aula116_2.py")
