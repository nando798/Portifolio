# Yield From
def gen1():
    print("comecou gen1")
    yield 1
    yield 2
    yield 3
    print("acabou gen1")


def gen2(gen=None):
    print("comecou gen2")
    if gen is not None:
        yield from gen()
    yield 4
    yield 5
    yield 6
    print("acabou gen2")


def gen3():
    print("comecou gen3")
    yield 10
    yield 20
    yield 30
    print("Acabou gen3")


g1 = gen2(gen1)
g2 = gen2(gen3)
g3 = gen3()

for numero in g1:
    print(numero)
print()

for numero in g2:
    print(numero)
print()

for numero in g3:
    print(numero)
print()
