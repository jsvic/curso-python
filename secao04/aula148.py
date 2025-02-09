def gen1():
    print('Começou o gen1')
    yield 1
    yield 2
    yield 3
    print('Acabou o gen1')


def gen2(gen):
    print('Começou o gen3')
    yield from gen()
    print('Acabou o gen3')


g1 = gen2(gen1)


for i in g1:
    print(i)
