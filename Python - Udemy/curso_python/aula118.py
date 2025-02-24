def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)

    return lista


cliente1 = adiciona_clientes("Fernando")
adiciona_clientes("Neide", cliente1)
cliente1.append("Claudio")

cliente2 = adiciona_clientes("Joana")
cliente2 = adiciona_clientes("Carla", cliente2)

cliente3 = adiciona_clientes("Claudineide")
cliente3 = adiciona_clientes("Dalva", cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
