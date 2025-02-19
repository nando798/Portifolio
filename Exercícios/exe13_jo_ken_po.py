import random

print("Boas vindas ao jogo de pedra, papel e tesoura!")
print("1. Pedra")
print("2. Papel")
print("3. Tesoura")
escolha = input("escolha uma opção: ")
print()
escolha_jogador = int(escolha)
escolha_computador = random.randint(1, 3)

print(f"a escolha do jogador foi: {escolha_jogador}")
print(f"a escolha do computador foi: {escolha_computador}")

if escolha_jogador == escolha_computador:
    print("empate!")

elif (
    (escolha_jogador == 1 and escolha_computador == 3)
    or (escolha_jogador == 2 and escolha_computador == 1)
    or (escolha_jogador == 3 and escolha_computador == 2)
):
    print("jogador ganhou!")
else:
    print("computador ganhou!")
