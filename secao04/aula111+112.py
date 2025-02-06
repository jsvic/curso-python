def soma1(*args):
    resposta = 0
    for i in args:
        resposta += i

    return resposta

operaacao = soma1(1, 2, 3, 4, 5, 6)

print(operaacao)

print('='*50)

def soma2(x, y, z):
    return x + y + z

numeros = [1, 2, 3]

print(soma2(*numeros))