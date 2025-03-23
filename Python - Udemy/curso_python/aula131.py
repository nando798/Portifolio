"""
@property - um getter no modo pythonico
getter - um metodo para obyter  um atributo
cor - get_cor()
modo pythonico - modo do python para fazer as coisas
@property é uma propriedade do objeto, ela é
um metodo que se comporta como um atributo
geralmente é usada nas seguintes situacoes:
- como getter
- para evitar quebra de codigo cliente
- para habilitar o setter
- para executar ações ao obter um atributo
"""


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print("PROPERTY")
        return self.cor_tinta


caneta = Caneta("Rosa")

print(caneta.cor)
