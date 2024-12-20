from restaurante import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato

restaurante_praca = Restaurante("praca", "gourmet")
bebida_suco = Bebida("Suco de melancia", 5.0, "grande")
prato_gourmet = Prato("Caviar", 1200.0, "Melhor um caviar do que um que vier")

restaurante_praca.adicionar_ao_cardapio(bebida_suco)
restaurante_praca.adicionar_ao_cardapio(prato_gourmet)

def main():
    print(bebida_suco)
    print(prato_gourmet)

if __name__ == "__main__":
    main()