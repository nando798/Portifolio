from veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, marca, modelo, esportiva):
        super().__init__(self, marca, modelo, esportiva)
        self._esportiva = True

    def __str__(self):
        return f"{self._esportiva}"
