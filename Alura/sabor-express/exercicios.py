# print("Pyhton na Escola de Programação Alura")


# nome = "Fernando"
# idade = 29

# print(f"Meu nome é {nome} e tenho {idade} anos")


# print("A", "L", "U", "R", "A", sep="\n")

# pi = 3.1415
# # arredondado = math.ceil(pi)
# print(f"O valor arredondado de pi é:', {pi:.2f}")

# print(
#     """Camiseta Unisex
#        Tamanho: P, M, G, GG
#        Material: 100% Algodão
#        Cores: Preto, Branco, Vermelho"""
# )

# =========================================\

# departamento = input("digite o nome do departamento: ")
# responsavel = input("digite o responsavel pelo departamento: ")
# print(f"O lider {responsavel} é responsável pelo departamento {departamento}")


# def classificar_musica(genero_favorito, genero_musica):
#     if genero_favorito == genero_musica:
#         return "recomendada"
#     elif genero_favorito == "Pop" or genero_favorito == "Rock":
#         return "neutra"
#     else:
#         return "não recomendada"


# resultado = classificar_musica("Rock", "Pop")
# print(resultado)

# ============================================

# numero = int(input("insira um numero de 0 a 10 "))

# if numero % 2 == 0:
#     print("numero par")
# else:
#     print("numero impar")

# idade = int(input("insira a sua idade: "))
# if idade >= 0 and idade <= 12:
#     print("Criança")
# elif idade >= 13 and idade <= 18:
#     print("Adolescente")
# else:
#     print("Adulto")

# ================================================

# senha = int(input("digite uma senha: "))
# nome_usuario = input("Digite o nome do usuário: ")

# if senha == 12345 and nome_usuario == "Fernando":
#     print("acesso concedido")
# else:
#     print("acesso negado")

# ==============================================

# coord_x = int(input("digite as coordendas x: "))
# coord_y = int(input("digite as coordendas y: "))

# if coord_x > 0 and coord_y > 0:
#     print("Primeiro Quadrante")
# elif coord_x < 0 and coord_y > 0:
#     print("Segundo Quadrante")
# elif coord_x < 0 and coord_y < 0:
#     print("Terceiro Quadrante")
# elif coord_x > 0 and coord_y < 0:
#     print("Quarto Quadrante")
# else:
#     print("O ponto está localizado no eixo de origem")


# ===========================================

# numero = -1

# while numero <= 0:
#     numero = int(input("digite um numero positivo: "))
#     print(f"Você digitou o numero {numero}")

# ===============================================

# projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]


# for projeto in projetos:
#     if projeto:
#         print(f"Projeto: {projeto}")
#     else:
#         print("Valor não encontrado")

# ============================================

# listaNum = 0
# listaNomes = ["Fernando", "Neide", "Dalva", "Joao"]
# ListIdade = ["1984", "2024"]
# for listaNum in range(1, 11):
#     if listaNum <= 10:
#         print(listaNum)
#     else:
#         print("numero inválido")

# ============================================

# for numero in range(1, 11):
#     if numero % 2 != 0:
#         listaNum += numero
#         print(f"A soma dos numeros impares é: {listaNum}")

# ===============================================

# numero = int(input("Digite um numero de zero a 10: "))

# print(f"Tabuada do {numero}")

# for item in range(1,10):
#     print(f"{numero} x {item} = {numero*item}")

# ================================================

# numeros = [65, 92, 25, 74, 109]
# soma = 0
# try:
#     for i in numeros:
#         soma += i
#     print(soma)
# except:
#     print("Ocorreu um erro no codigo")

# ================================================

# lista_numeros = [65, 92, 25, 74, 109]

# try:
#     for item in lista_numeros:
#         media = int(sum(lista_numeros) / len(lista_numeros))
#     print(media)
# except:
#     print("Ocorreu um erro no programa")

# ================================================


# for i in range(10, 0, -3):
#     print(i)


# =================================================

# livro = {
#     "titulo": "Aprendendo Python",
#     "autor": "Fabrício Silva",
#     "ISBN": "12345",
#     "preco": 59.90,
#     "em_estoque": True,
# }

# livro["preco"] = 69.90
# print(livro["preco"])

# =================================================

# credenciais_clientes = {
#     "alice123": {
#         "username": "alice123",
#         "password": "alic3P@ssw0rd",
#         "status": "active",
#     },
#     "bob456": {"username": "bob456", "password": "b0bP@ssword!", "status": "inactive"},
#     "charlie789": {
#         "username": "charlie789",
#         "password": "Ch@rlieP@ss9",
#         "status": "active",
#     },
# }

# alerta = (
#     "Enviar Alerta"
#     if credenciais_clientes["bob456"]["status"] == "inactive"
#     else "Sem alerta"
# )
# print(alerta)


# =================================================
# dados_pessoa = {}


# dados_pessoais = {
#         "nome": "Calango",
#         "idade": 530,
#         "cidade": "Xique-Xique-Bahia",
#     }

# dados_jogo = {
#         "jogo": "Minecraft",
#         "lancamento": 1530,
#         "produtora": "Mojang",
#     }

# dados_pessoa.update(dados_pessoais)
# dados_pessoa.update(dados_jogo)

# print(dados_pessoa["nome"])

##===============================================


# "Imagine que você tem uma caixa de brinquedos e quer saber quantos brinquedos de cada tipo você tem."
def contar_palavras(frase):
    """Conta a frequência de cada palavra em uma frase.

    Args:
      frase: A frase a ser analisada.

    Returns:
      Um dicionário onde as chaves são as palavras e os valores são as suas frequências.
    """

    contagem_palavras = {}

    palavras = frase.lower().split()  # type: ignore

    for palavra in palavras:
        if palavra in contagem_palavras:
            contagem_palavras[palavra] += 1
        else:
            contagem_palavras[palavra] = 1
    return contagem_palavras


frase = "Imagine que você tem uma caixa de brinquedos e quer saber quantos brinquedos de cada tipo você tem."
resultado = contar_palavras(frase)
print(resultado)
