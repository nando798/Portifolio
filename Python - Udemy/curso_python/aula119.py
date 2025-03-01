# Exercício - Lista de tarefa com desfazer e refazer
# todo = [] -> lista de tarefa
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
import json

arquivo_tarefas = "tarefas.json"


def salvar_arquivos(tarefas, tarefas_refazer):
    # salva os arquivos em um arquivo JSON.
    with open(arquivo_tarefas, "w") as arquivo:
        json.dump(
            {"tarefas": tarefas, "tarefas_refazer": tarefas_refazer}, arquivo, indent=4
        )


def carregar_tarefas():
    # carrega as tarefas de um arquivo JSON, se ele existir.
    if os.path.exists(arquivo_tarefas):
        with open(arquivo_tarefas, "r", encoding="utf-8") as arquivo:
            try:
                dados = json.load(arquivo)
                return dados.get("tarefas", []), dados.get("tarefas_refazer", [])
            except json.JSONDecodeError:
                print("erro ao carregar o arquivo JSON. Iniciando listas vazias.")
    return [], []


CAMINHO_ARQUIVO = "aula119.json"


def listar(tarefa):
    if not tarefas:
        print("nenhuma tarefa")
        return

    print("tarefas:")
    for tarefa in tarefas:
        print(f"\t{tarefa}")
    print()


def desfazer(tarefa, tarefas_refazer):
    if not tarefa:
        print("não há nada a desfazer")
        return

    tarefa = tarefas.pop()
    print(f"{tarefa} removida da lista de tarefas")
    tarefas_refazer.append(tarefa)
    listar(tarefas)


def refazer(tarefa, tarefas_refazer):
    if not tarefas_refazer:
        print("não há nada a refazer")
        return

    tarefa = tarefas_refazer.pop()
    print(f"{tarefa} adicionada na lista de tarefas.")
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    if not tarefa:
        print("você nao digitou nenhuma tarefa")
        return
    tarefa = tarefa.strip()
    tarefas.append(tarefa)
    print(f"{tarefa} foi adicionado a lista de tarefas")
    listar(tarefas)


tarefas = []
tarefas_refazer = []


while True:
    print()
    print("Comandos: listar, desfazer e refazer")
    tarefa = input("Digite uma tarefa ou comando: ")

    comandos = {
        "listar": lambda: listar(tarefa),
        "desfazer": lambda: desfazer(tarefa, tarefas_refazer),
        "refazer": lambda: refazer(tarefa, tarefas_refazer),
        "clear": lambda: os.system("clear"),
        "adicionar": lambda: adicionar(tarefa, tarefas),
    }
    comando = (
        comandos.get(tarefa)
        if comandos.get(tarefa) is not None
        else comandos["adicionar"]
    )

    comando()
    salvar_arquivos(tarefas, tarefas_refazer)
