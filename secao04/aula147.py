def generator(n = 0):
    yield n + 3
    return 'Acabou'

gen = generator(4)


print(next(gen))

print('=' * 50)

def generator(inicio = 0, fim = 10):
    while True:
        yield inicio
        inicio += 1

        if inicio >= fim :
            return

g1 = generator()
g2 = (n for n in range(10))

for i in g1:
    print(i)

print('-' * 50)

for i in g2:
    print(i)