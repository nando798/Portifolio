# ps/listdir pata navegar em caminhos
# D:\Wallpapers

# caminho = r"D:\\Wallpapers"
import os

caminho = os.path.join(r"D:\Wallpapers")

for imagem in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, imagem)
    print(caminho_completo)  # Corrigido: junta o caminho base com a pasta
    if not os.path.isfile(caminho_completo):
        continue
    print("Imagem:", imagem)  # Corrigido: imprime o nome da imagem
# Corrigido: junta o caminho base com a pasta
