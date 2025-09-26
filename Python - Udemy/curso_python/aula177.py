# # json.dunp e json,load com aerquivos

# import json
# import os

# NOME_ARQUIVO = "aula177.json"
# CAMINHO_ABSOLUTO = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)
# )

# filme = {
#     "filme": "O senhor dos Anéis: A Sociedade do Anel",
#     "nome_original": "The Lord of the Rings: The Fellowship of the Ring",
#     "ano": 2001,
#     "diretor": "Peter Jackson",
#     "atores": ["Elijah Wood", "Ian McKellen", "Orlando Bloom", "Cate Blanchett"],
#     "genero": "Fantasia",
# }

# with open(CAMINHO_ABSOLUTO, "w", encoding="utf-8") as f:
#     json.dump(filme, f, ensure_ascii=False, indent=2)


# with open(CAMINHO_ABSOLUTO, "r", encoding="utf-8") as f:
#     filme_json = json.load(f)

# # print(filme)
# print(filme_json)


from pathlib import Path

# caminho_projeto = Path()
# print(caminho_projeto.absolute())

arquivo = Path.home() / "Desktop" / "aula177.txt"
print(arquivo.touch())
print(arquivo)
arquivo.write_text("Olá Mundo!")
