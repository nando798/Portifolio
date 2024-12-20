from avaliacao import Avaliacao
from cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        self._cardapio = []

    def __str__(self):
        return f"{self.nome} | {self.categoria}"

    @classmethod
    def listar_restaurantes(cls):
        header = f"{'Nome do Restaurante'.ljust(25).upper()} | {'Categoria do Restaurante'.ljust(25).upper()} |{'Avaliação'.ljust(25)} | {'Status'.upper()}"
        print(header)
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes()).ljust(24)} | {restaurante._ativo}"
            )

    @property
    def ativo(self):
        return "✔" if self._ativo == True else "✘"

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    def media_avaliacoes(
        self,
    ):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_ao_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f"cardapio do restaurante {self._nome}\n")
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, "descricao"):
                mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | {item.descricao}"
                print(mensagem_prato)
            else:
                mensagem_bebida = (
                    f"{i}. Nome: {item._nome} | Preço: R${item._preco} | {item.tamanho}"
                )
                print(mensagem_bebida)
