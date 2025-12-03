# Pillow: redimensionando imagens com Python
# Essa biblioteca é o photoshop do python
from pathlib import Path
from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / "desenho.png"
NEW_IMAGE = ROOT_FOLDER / "cartoon.png"

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size 
# print(f"Tamanho original da imagem: {width}x{height}")
exif = pil_image.info["exif"]  # Mantém os metadados da imagem original


new_width = 544
new_height = round(height * new_width / width)
# print(f"o novo tamanho da imagem é: {new_height}x{new_width}")

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(NEW_IMAGE, optmize=True, quality=95)  # , exif=exif