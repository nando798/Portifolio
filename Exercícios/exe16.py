# INICIAR programa

# IMPORTAR biblioteca de caracteres e geração aleatória

# FUNÇÃO gerar_senha(tamanho)
#     DEFINIR caracteres como letras + números + símbolos
#     DEFINIR senha como string vazia
#     PARA i de 1 até tamanho FAÇA
#         ESCOLHER um caractere aleatório dos caracteres
#         ADICIONAR caractere à senha
#     FIM PARA
#     RETORNAR senha

# LER tamanho da senha do usuário
# SE tamanho for um número válido ENTÃO
#     senha_gerada ← chamar FUNÇÃO gerar_senha(tamanho)
#     EXIBIR "Sua senha gerada é:", senha_gerada
# SENÃO
#     EXIBIR "Entrada inválida. Digite um número inteiro."
# FIM SE

# FINALIZAR programa
import random
import string


def gerador_senha(tamanho):
    caracteres = string.ascii_lowercase + string.ascii_letters + string.digits

    senha = ""
    for i in range(10):
        senha += random.choice(caracteres)
    return senha


print(gerador_senha(10))
