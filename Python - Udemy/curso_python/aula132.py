"""
@property - um setter no modo pythonico
`setter - um metodo pasras definir um atributo
- como getter
- para evitar quebra de codigo cliente
- para habilitar o setter
- para executar ações ao obter um atributo
Atributos que começam com um ou dois uderlines
nao devem ser usados fora da classe
"""


class Caneta:
    def __init__(self, cor):
        # private, protected, public
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print("Property")
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor == "Pink":
            raise ValueError("Cor não pode ser Pink!")
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta("Rosa")
caneta.cor = "Rosa"
# mostrar(caneta)

caneta._cor_tampa = "Black"
print(caneta.cor)
print(caneta.cor_tampa)
