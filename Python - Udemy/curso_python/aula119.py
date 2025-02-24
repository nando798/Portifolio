# Exercício - Lista de tarefa com desfazer e refazer
# todo = [] -> lista de tarefa
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


tarefa = []
desfazer = []
refazer = []


while True:
    print()
    print("Tarefas:")
    print("1. Adicionar")
    print("2. Desfazer")
    print("3. Refazer")
    print("4. Sair")
    print()
    nova_tarefa = input("Escolha uma das opções:")

    if nova_tarefa.lower() == "1":
        tarefa_real = input("Digite a nova tafera: ")
        tarefa.append(tarefa_real)
        print("tarefa adicionada, lista atual: ", tarefa)
        print()
    elif nova_tarefa.lower() == "2":
        if not tarefa:
            print("Não há o que desfazer")
            print()
        else:
            ultima_tarefa = tarefa.pop()
            desfazer.append(ultima_tarefa)
            print("tarefa desfeita", tarefa)
            print()

    elif nova_tarefa.lower() == "3":
        if not desfazer:
            print("não há o que desfazer")
        else:
            tarefa_restaurada = desfazer.pop()
            tarefa.append(tarefa_restaurada)
            print("tarefa refazer", tarefa)

    elif nova_tarefa.lower() == "4":
        print("até mais")
        print()
        break
