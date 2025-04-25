"""
abstractmethod para qualquer metodo ja decorado
é possivel criar um @proeprtry, @property.setter, @classmethod, @staticmethod e
@method e metodos normais como abstratos, para isso use o @abstractmethod como
decorator mais interno.
Foo - Bar são palavras usadas como placeholder para palavras que podem
mudar na programacao.
"""

from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = name
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self):
        return self._name


class Foo(AbstractFoo):

    def __init__(self, name):
        super().__init__(name)
        # print("Sou inutil")

    @AbstractFoo.name.setter
    def name(self, name): 
        self._name = name


foo = Foo("Barra de torcao a 376 graus")
print(foo.name)
