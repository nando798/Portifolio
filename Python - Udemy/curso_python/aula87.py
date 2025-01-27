# isinstace - para saber se objeto é de determinado tipo
lista = [
    "a",
    1,
    1.1,
    True,
    [0, 1, 2],
    (1, 2),
    {0, 1},
    {"nome": "Luiz"},
]

for item in lista:

    if isinstance(item, set):
        print("SET")
        item.add(6)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print("STR")

        print(item, isinstance(item, set))

    elif isinstance(item, float):
        print("FLOAT")
        print(item, isinstance(item, set))

    elif isinstance(item, (int, float)):
        print("NUMERO:")
        print(item, item * 3)
    else:
        print("OUTRO")
        print(item)
