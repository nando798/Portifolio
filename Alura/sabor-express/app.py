import os

# dicionário de restaurantes
restaurantes = [
    {"nome": "Burger King", "categoria": "Fast-Food", "ativo": True},
    {"nome": "Buffalo Grill", "categoria": "Churrasco", "ativo": False},
    {"nome": "China In Box", "categoria": "japonesa", "ativo": True},
]


# exibe o nome do programa
def exibir_nome_programa():

    print(
        """Sabor Express
        """
    )


# mostra as opcoes do restaurante
def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Alternar Estado do Restaurante")
    print(
        """4. Sair
        """
    )


# finaliza o programa
def finalizar_app():
    subtitulos("finalizar Programa")


def subtitulos(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def menu_principal():
    input("\nDigite uma tecla para voltar ao menu ")
    main()


def opcao_invalida():
    print("Opção Inválida!\n")
    menu_principal()


def cadastrar_novo_restaurante():
    """Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
     Adiciona um novo restaurante a lista de restaurantes

    """

    subtitulos("Cadastro de Novos Restaurantes:")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(
        f"Digite a categoria do {nome_do_restaurante} que deseja cadastrar: "
    )
    dados_do_restaurante = {
        "nome": nome_do_restaurante,
        "categoria": categoria,
        "ativo": False,
    }
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso")
    menu_principal()


def listar_restaurantes():
    subtitulos("Listando Restaurantes")
    print(f" {"Nome".ljust(16)} | {"Categoria".ljust(16)} | {"Status"}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        nome_categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(
            f" .{nome_restaurante.ljust(15)} | .{nome_categoria.ljust(15)} | .{ativo}"
        )

    menu_principal()


def alterar_estado_restaurante():
    subtitulos("Alterando Estado do Restaurante")
    nome_restaurante = input(
        "Digite o nome do restaurante que deseja alterar o estado: "
    )
    restaurante_escontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_escontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = (
                f"o restaurante {nome_restaurante} foi ativado com sucesso"
                if restaurante["ativo"]
                else f"O restaurante foi desativado com sucesso"
            )
            print(mensagem)
    if not restaurante_escontrado:
        print("O restaurante não foi encontrado")


def opcao_escolha():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        match opcao_escolhida:

            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()

    except:
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    opcao_escolha()


if __name__ == "__main__":
    main()
