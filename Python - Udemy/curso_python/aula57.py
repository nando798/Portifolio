salas = [
    ["maria", "helena",],
    ["elaine", "eliane"],
    ["luiz", "joao", "eduarda",]]


# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f"os alunos dessa sala são:")
    for aluno in sala:
         print(aluno)