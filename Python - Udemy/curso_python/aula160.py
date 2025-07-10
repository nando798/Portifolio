# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple
from typing import NamedTuple


class Carta(NamedTuple):
    valor: str = "Valor"
    naipe: str = "Naipe"


# carta = namedtuple(
#     "Carta",
#     ["valor", "naipe"],
#     defaults=["VALOR", "NAIPE"],
# )
as_espada = Carta("A", "♠")
# print(as_espada)
# print(as_espada[1])  # Acessando os valores
print(Carta._field_defaults)  # Acessando os valores padrão
for valor in as_espada:
    print(valor)
