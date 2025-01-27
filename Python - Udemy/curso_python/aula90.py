# Generator Expression, iterables and Iterators in Python
import sys

iterable = ["Eu", "Tenho", "__iter__"]
iterator = iterable.__iter__()  # tem __iter__ e __next__
lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

for i in generator:
    print(i)
