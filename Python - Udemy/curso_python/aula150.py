# Context Manager com funções - Criando e Usando gerenciadores de contexto

from contextlib import contextmanager


@contextmanager
def MyOpen(caminho_arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(caminho_arquivo, modo, encoding="utf-8")
        yield arquivo
    except Exception as e:
        print("Erro:", e)
    finally:
        print("Fechando arquivo")
        arquivo.close()


with MyOpen("aula150.txt", "w") as arquivo:
    arquivo.write("arquivo 546\n")
    arquivo.write("arquivo 837\n")
    arquivo.write("arquivo 927\n")
    arquivo.write("arquivo 684 \n")
    print("Dentro do with", arquivo)
