# a = 18
# b = 0

try:
    a = 18
    b = 0
    # print(b[0])
    print("Linha 1"[1000])
    c = a / b
    print("Linha 2")

except ZeroDivisionError as error:
    print("Erro, não é possivel dividir por zero...", error.__class__.__name__)
    print(error)

except NameError:
    print("Nome 'b' não definido")

except (TypeError, IndexError) as error:
    print("TypeError + IndexError")
    print("Mensagem:", error.__class__.__name__)

except Exception:
    print("Erro desconhecido...")
print("Continuar")
