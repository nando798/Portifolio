"""
Encapsulamento (modificadores de acesso: public, private, protected)
Python não tem modificadores de acesso
mas podemos seguir as seguintes convenções
(sem underline) = public
pode ser usado em qualquer lugar
(um underline) = protected
não deve ser usado fora da classe e nas subclasses.
(dois underlines) = private
"name mangling"(desfiguração de nomes) em python
só deve ser usado na classe em que foi declarado
"""

from functools import partial


class Foo:
    def __init__(self):
        self.public = "método publico"
        self._protected = "método protegido"
        self.__private = "método privado"

    def public_method(self):
        self._protected_method()
        print(self._protected)
        self.__private_method()
        print(self.__private)
        return "public_method"

    def _protected_method(self):
        print("_protected_method")
        return "_protected_method"

    def __private_method(self):
        print("__private_method")
        return "__private_method"


f = Foo()
print(f.public_method())
