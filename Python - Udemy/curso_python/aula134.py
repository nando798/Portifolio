"""
Relação entre classes: associação, agregação e composição
Associação é uma tipo ded relação onde os objetos estão
ligados dentro do sistema.
Essa é a relação mais comum entre onjetos e tem subconjuntos
como agregação e composição.
Geralmente, temops um a associação quando um objeto tem um atributo
que referencia outro objeto.

"""


class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f"escrevendo com a {self.nome}"


caneta = FerramentaEscrever("caneta Bic")
maquina_escrever = FerramentaEscrever("maquina de escrever")
escritor = maquina_escrever

escritor.ferramenta = maquina_escrever

print(caneta.escrever())
# print(caneta.escrever())
print(escritor.ferramenta.escrever())
