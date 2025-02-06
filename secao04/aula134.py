def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def criar_multiplicador(qnt):
    def multiplicar(n):
        return n * qnt
    return multiplicar

print(executa(lambda x, y: x + y, 1, 2))
print(soma(1, 2))

print('=' * 50)

dobro1 = criar_multiplicador(2)
dobro2 = executa(lambda qnt : lambda n : qnt * n, 2)

print(dobro1(2))
print(dobro2(2))