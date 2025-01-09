"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista_compras = []


while True:
    print("1. Adicionar | 2. Remover | 3. Listar | 4. Sair")
    opcao_usuario = input("Digite a opcao desejada: ")
   
    if opcao_usuario == "1":
        opcao1 = input("Digite o item a ser adicionado: ")
        lista_compras.append(opcao1)
        print("Item adicionado.")
        
    elif opcao_usuario == "2":
        if len(lista_compras) == 0:
            print("Sua lista está vazia")
        else:
            for i, item in enumerate(lista_compras): 
                print(f"{i}, {item}")
            try:
                indice = int(input("Digite o item a ser removido: "))
                if indice >= 0 or indice < len(lista_compras):
                    removido = lista_compras.pop(indice)
                    print(f"o item {removido} foi removido\n")
                    os.system("cls")
                else:
                    print("numero invalido")
            except Exception:
                print("Erro desconhecido")
            except ValueError:
                print("Erro de valor")
    elif opcao_usuario == "3":
        if len(lista_compras) == 0:
            print("lista Vazia")   
             
        else:
            for i, item in  enumerate(lista_compras):
                print(f"{i}, {item}")  

    elif opcao_usuario == "4":
        print("Sair do programa")    
        break
    else:
        print("Opcao inválida")





