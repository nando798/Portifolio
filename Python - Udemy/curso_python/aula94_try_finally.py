# try, else and finally in Python

try:
    print("fernando")
    8 / 0

except ZeroDivisionError as error:
    print("Erro: Não pode dividir por zero!", error.__class__.__name__)
    print(error)
except (NameError, ImportError) as error:
    print("Erro: Erro de importação", error.__class__.__name__)
    print(error)
except IndexError as error:
    print("Erro: IndexError", error.__class__.__name__)
    print(error)
else:
    print("Não deu erro")
finally:
    print("Neide")
