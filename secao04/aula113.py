# Exercício 1
def multiplicar(*args):
    resposta = 1

    for i in args:
        resposta *= i
    
    return resposta

print(multiplicar(1, 2, 3))

# Exercício 2
def tipo_num(num):
    if num % 2 == 0:
        return 'Par'
    
    return 'Impar'

print(tipo_num(2))
print(tipo_num(3))