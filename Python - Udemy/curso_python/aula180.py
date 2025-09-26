import csv
from pathlib import Path


CAMINHO_CSV = Path(__file__).parent / "aula180.csv"
lista_clientes = [
    {"Nome": "João", "Idade": 30, "Endereço": "Rua A, 123"},
    {"Nome": "Maria", "Idade": 25, "Endereço": "Rua B, 456"},
    {"Nome": "Pedro", "Idade": 35, "Endereço": "Rua C, 789"},
]

with open(CAMINHO_CSV, "w", encoding="utf-8", newline="") as f:
    nomes_colunas = [lista_clientes[1].keys()]
    escritor_csv = csv.writer(f)
    escritor_csv.writerow(nomes_colunas)

    for cliente in lista_clientes:
        escritor_csv.writerow([cliente])

    print(f"Arquivo {lista_clientes} criado com sucesso!")
