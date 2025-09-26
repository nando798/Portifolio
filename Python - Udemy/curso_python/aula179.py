# csv.reader e csv.DictReader
# dcsv.reader  lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "aula178-ex.csv"

# print(CAMINHO_CSV.exists())

with open(CAMINHO_CSV, "r", encoding="utf-8") as f:
    leitor_csv = csv.DictReader(f)
    print(next(leitor_csv))

    for linha in leitor_csv:
        print(linha["Nome"], linha["Idade"], linha["Endereço"])
