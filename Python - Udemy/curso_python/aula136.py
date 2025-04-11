# Relacoes entre classes: associacao, agregacao e composicao
# Composicao é uma especializacao de agregacao.
# Mas nela, quando o objeto "pai" é apagado, todas as referencias
# dos objetos "filhos" tambem serao apagados.


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print("Apagando", self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print("Apagando", self.rua, self.numero)


cliente1 = Cliente("Maria")
cliente1.inserir_endereco("Rua Originals", 543)
cliente1.inserir_endereco("Rua piratas", 345)
endereco_externo = Endereco("Estrada das Lagrimas", 6562)
cliente1.inserir_endereco_externo(endereco_externo)

print(cliente1.enderecos[0].rua)
print(cliente1.enderecos[1].rua)
cliente1.listar_endereco()

print()
print("############################")
print()




