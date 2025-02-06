def nome():
    print('várias')

nome()  

print('='*50)

def imprimir(a, b):
    print(a)
    print(b)

imprimir('nome1', 'nome2')

print('='*50)

def saudacao(nome = 'sem nome'):
    print(f'Olá, {nome}!')

saudacao('José')
saudacao()