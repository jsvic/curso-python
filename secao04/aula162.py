def soma(x : 0, y : 0):
    return x + y


def multiplica(x: 1, y: 1):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(2))
print(multiplica_por_dez(2))