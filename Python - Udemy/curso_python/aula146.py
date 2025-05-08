# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)


class MyError(Exception): ...


class OtherError(Exception): ...


def levantar():
    meuerro = MyError("meu erro...", "nosso erro...", "o erro deles...")
    meuerro.add_note("isso é uma primeira nota...")

    raise meuerro


try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    meuerro = OtherError("voulancar de novo o erro...")
    meuerro.add_note("isso é uma nota...")
    meuerro.__notes__ += error.__notes__.copy()
    raise meuerro from error
