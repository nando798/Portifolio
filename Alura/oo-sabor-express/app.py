from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.restaurante import Restaurante

# Criando restaurante e adicionando avaliações
restaurante_mexicano = Restaurante("Mexicano", "Gourmet")
cardapio_prato = Prato("Burrito", 25.0, "O melhor burrito da cidade")
cardapio_bebida = Bebida("Limonda Suiça", 6.0, "500 ml")
restaurante_mexicano.adicionar_ao_cardapio(cardapio_bebida)
restaurante_mexicano.adicionar_ao_cardapio(cardapio_prato)


def main():
    restaurante_mexicano.exibir_cardapio


# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()
