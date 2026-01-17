import os
import shutil

PASTA_ORIGEM = "teste"

EXTENSIONS = {
    "imagens": [".jpg", ".png"],
    "pdf": [".pdf"], 
    "excel": [".xls", ".xlsx"],
}

arquivos = os.listdir(PASTA_ORIGEM)

for pasta in EXTENSIONS:
    caminho_pasta = os.path.join(PASTA_ORIGEM, pasta)
    os.makedirs(caminho_pasta, exist_ok=True)
    # print(f'Pasta {pasta} criada com sucesso!')

for file in arquivos:
    caminho_completo = os.path.join(PASTA_ORIGEM, file)

    if os.path.isfile(caminho_completo):
        name, extension = os.path.splitext(file) 
        print(file, "->", extension) 

        for pasta, list_extensions in EXTENSIONS.items():
            if extension in list_extensions:
                destino = os.path.join(PASTA_ORIGEM, pasta, file)
                shutil.move(caminho_completo, destino)
                print(f"{file} move to {pasta}")
                break