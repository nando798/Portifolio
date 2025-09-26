# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
import json
# from pprint import pprint
from typing import TypedDict


class Filme(TypedDict):
    filme: str
    nome_original: str
    ano: int
    diretor: str
    atores: list[str]
    genero: str


string_json = """
{
    "filme": "O senhor dos Anéis: A Sociedade do Anel",
    "nome_original": "The Lord of the Rings: The Fellowship of the Ring",
    "ano": 2001,
    "diretor": "Peter Jackson",
    "atores": [
        "Elijah Wood",
        "Ian McKellen",
        "Orlando Bloom",  
        "Cate Blanchett"
    ],
    "genero": "Fantasia"
}
"""
# print(string_json)

movie: Filme = json.loads(string_json)

print(json.dumps(movie, ensure_ascii=False, indent=1))


# print(movie["filme"])
# pprint(movie)
# print(movie["nome_original"])
