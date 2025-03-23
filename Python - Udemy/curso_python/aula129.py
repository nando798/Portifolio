# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.


class Classe:
    @staticmethod
    def funcao_dentro_da_classe(*args, **kwargs):
        print("Olá, você está dentro da classe", args, kwargs)


c1 = Classe()

c1.funcao_dentro_da_classe(1, 2, 3)
Classe.funcao_dentro_da_classe(nomeado=5)
