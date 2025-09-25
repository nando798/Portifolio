# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv
args = len(argumentos)

if args <= 1:
    print(f"Nenhum argumento foi passado para o sistema.")
else:
    print(f"Foram passados {args - 1} argumentos para o sistema.")
