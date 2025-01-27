# dir, hasattr e getattr em pyhon

string = "fernando"
metodo = "lower"


if hasattr(string, metodo):
    print("existe um upper aqui")
    print(getattr(string, metodo)())
else:
    print("Não existe o método", metodo)
