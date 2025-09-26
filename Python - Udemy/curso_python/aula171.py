"""
os.walk
os.walk é uma função que permirre percorrer uma estrutura de diretórios de maneira recursiva.
Ela gera uma sequencia de tuplas, onde cada tupla possui tres elementos: o diretorio atual(root),
uma lista de subdiretorios (dirs) e uma lista dos arquicvos do diretorio atual(files).
"""

import os

from itertools import count

caminho = os.path.join(r"D:\\Wallpapers")
counter = count()
for root, dirs, files in os.walk(caminho):
    the_count = next(counter)
    # print(the_count, "pasta atual", the_count, files)

    for dir_ in dirs:
        print("subpasta", the_count, dir_)
    print()

    for file_ in files:
        print(f"Aqruivo: {the_count}", file_)
