# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / "aula183.txt"

locale.setlocale(locale.LC_ALL, "")


def converte_brl(numero: float) -> str:
    brl = "R$" + locale.currency(numero, grouping=True, symbol=False)

    return brl


data = datetime(2025, 9, 9)
dados = dict(
    nome="fernando",
    valor=converte_brl(1267.80),
    data=data.strftime("%d/%m/%Y"),
    empresa="neifecakes",
    telefone="(11) 968423860",
)

import json


class MyTemplate(string.Template):
    delimiter = "$"


with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

    template = MyTemplate(texto)
    print(template.substitute(dados))
