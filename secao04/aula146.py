import sys

lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(generator)

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))