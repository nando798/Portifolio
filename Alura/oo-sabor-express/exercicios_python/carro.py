from exercicios_python.veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(self, marca, modelo, portas)
        self._portas = portas

    def __str__(self):
        return f"{self._marca} | {self._modelo} | {self._portas}"
