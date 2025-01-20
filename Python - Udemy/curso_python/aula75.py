# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def multiplicar(multi):
    def multiplicamento(numero):
        return numero * multi

    return multiplicamento


total = multiplicar(4)
duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadruplicar = multiplicar(4)
print(total(2))
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
