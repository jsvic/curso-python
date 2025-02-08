dicionario = {}
lista = []
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
intervalo = range(0, 0)


lista2= [0]
string2 = '0'

def tipo(valor):
    return 'Truthy' if  valor else 'Falsy'

print(f'{lista2=} {tipo(lista2)}')
print(f'{string2=} {tipo(string2)}')
print(f'{dicionario=} {tipo(dicionario)}')
print(f'{lista=} {tipo(lista)}')
print(f'{conjunto=} {tipo(conjunto)}')
print(f'{tupla=} {tipo(tupla)}')
print(f'{string=} {tipo(string)}')
print(f'{inteiro=} {tipo(inteiro)}')
print(f'{flutuante=} {tipo(flutuante)}')
print(f'{nada=} {tipo(nada)}')
print(f'{intervalo=} {tipo(intervalo)}')