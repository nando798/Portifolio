# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import pdfplumber

# PDF = Path(__file__).parent / "pdfs" / "R20251017.pdf"

# with pdfplumber.open(PDF) as pdf:
#     print("Páginas:", len(pdf.pages))
#     for i, page in enumerate(pdf.pages):
#         text = page.extract_text()
#         print(f"--- Página {i} ---")
#         if text:
#             print(text[:300])  # trecho do texto
#         else:
#             print("Nenhum texto extraído.")

#         # extrai tabelas (retorna lista de tabelas como lista de linhas)
#         tables = page.extract_tables()
#         if tables:
#             print(
#                 "Tabelas encontradas:", len(tables)
#             )  # primeiras 5 palavras da primeira tabela

#             # extrai imagens (retorna lista de dicionarios com metadados das imagens)
#         words = page.extract_words()
#         if words:
#             print(f"Exemplo palavra:", words[:5])  # primeiras 5 palavras extraídas

#         for img_idx, img in enumerate(page.images, start=1):
#             print(
#                 f"Imagem {img_idx} - bbox:", img.get("x0"), img.get("y0")
#             )  # metadados da imagem


# if not PDF.exists():
#     print("Arquivo PDF não encontrado:", PDF)
#     raise SystemExit(1)
# try:
#     with pdfplumber.open(PDF) as pdf:
#         print("Número de páginas no PDF:", len(pdf.pages))
#         pass
# except Exception as e:
#     print("Erro ao abrir o PDF com pdfplumber:", e)


PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / "pdfs"
PASTA_NOVA = PASTA_RAIZ / "novos_pdfs"
REL_BACEN = PASTA_ORIGINAIS / "R20251017.pdf"

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(REL_BACEN)

page = reader.pages[0]


with pdfplumber.open(REL_BACEN) as pdf:
    page_plumber = pdf.pages[0]
    if not page_plumber.images:
        print("nenhuma imagem encontrada na página 0")
    else:
        imagem0 = page_plumber.images[0]
        nome = imagem0.get("name", "img0.bin")
        # pdfplumber não traz os dados binários diretamente, apenas metadados
        # Para extrair a imagem, você precisa usar o bbox para recortar a área da imagem
        # Exemplo de extração usando bbox:
        bbox = (imagem0["x0"], imagem0["top"], imagem0["x1"], imagem0["bottom"])
        cropped = page_plumber.crop(bbox)
        img = cropped.to_image(resolution=150)
        img.save(PASTA_NOVA / f"{nome}.png")
        print(f"imagem salva, {PASTA_NOVA / f'{nome}.png'}")


for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f"page2{i}.pdf", "wb") as arquivo:
        writer.add_page(page)
        writer.write(arquivo)
