from dataclasses import dataclass, field


@dataclass
class Pessoa:
    nome: str = field(DEFAULT="Missing", repr=False)
    sobrenome: str

    def __post_init__(self):
        self.nome_sobrenome = f"{self.nome} {self.sobrenome}"

    # @property
    # def nome_sobrenome(self):
    #     return f"{self.nome} {self.sobrenome}"

    # @nome_sobrenome.setter
    # def nome_sobrenome(self, valor):
    #     nome, sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = sobrenome


if __name__ == "__main__":
    # Exemplo de uso
    p1 = Pessoa("João", "Souza")
    print(p1.nome_sobrenome)
    p1.nome_sobrenome = "Mariana Souza"
    print(p1.nome_sobrenome)
