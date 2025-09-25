from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-b",
    "--basic",
    help='Mostra "Ola mundo" na tela.',
    # type=str, #tipo do argumento
    metavar="STRING",
    # default="Olá Mundo", #valor padrao
    required=False,
    action="append",
    #nargs="+",
)
args = parser.parse_args()

if args.basic is None:
    print("Voce nao passou o valor de basic.")
    print(args.basic)
else:
    print(f"O valor de basic é {args.basic}.")
