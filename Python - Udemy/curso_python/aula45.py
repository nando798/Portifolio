"""
Iterável -> str, range, etc...
Iterador - quem sabe entregar um valro por vez
next -> me entregue o proximo valor
inter -> me entregue seu iterador

print(next(texto))

texto = "fernando"
iterator = iter(texto)

while True:
    try:
        palavra = next(iterator)
        print(palavra)
    except StopIteration:
        break

"""
texto = iter("Fernando")
for letra in texto:
    print(letra)