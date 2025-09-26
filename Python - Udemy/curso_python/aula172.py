# os.path.getsize e os.stat para dados dos arquivos
import math
import os
from itertools import count


def convert_size(size_bytes):
    if size_bytes <= 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1000)))
    p = math.pow(1000, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


caminho = os.path.join(r"D:\\Wallpapers")

counter = count()
for root, dirs, files in os.walk(caminho):
    the_count = next(counter)
    # print(the_count, "pasta atual", the_count, files)

    for dir_ in dirs:
        print("subpasta", the_count, dir_)
    print()

    for file_ in files:

        caminho_completo = os.path.join(root, file_)
        tamanho = os.path.getsize(caminho_completo)

        print(f"Aqruivo:", root, file_, convert_size(tamanho))
