"""
Relações entre classes: associacao, agrgacao e composicao
Agregacao é uma forma mais especializada de associacao
entre dois ou mais objetos. Cada objeto terá se ciclo de
vida independente.
Geralmente é uma relacao de um para muitos, onde um objeto
tem um ou muitos onjetos.
Os objetos podem, viver separadamente, mas pode se tratar
de uma relacxao onde o objeto precisa de outro para fazewr
determinada tarefa.
(existem controvérsias sobre as definicoes de agregacao).

"""


class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto("hylux", 100000), Produto("bmw", 150000)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
