# variavais livres + nonlocal (locals, globals)
def fora(x):
    a = x

    def dentro():
        return a

    return dentro


dentro1 = fora(2)
dentro2 = fora(5)

print(dentro1())
print(dentro2())
