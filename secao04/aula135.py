pessoa = {
    'nome' : 'josé',
    'sobrenome' : 'silva',
}

a, b = pessoa
print(a)
print(b)
print('=' * 50)

c, d = pessoa.values()
print(c)
print(d)
print('=' * 50)

(e1, e2), f = pessoa.items()
print(e1, e2)
print(f)
print('=' * 50)

dados_pessoa = {
    'idade' : 17,
    'altura' : 1.69,
}

pessoa_completa = {**pessoa, **dados_pessoa}


print(pessoa_completa)
print('=' * 50)

def mostrar_argumentos(*args, **kwargs):
    print('Não nomeados: ', args)

    print('Nomeados:')
    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_argumentos(1, 2, **pessoa_completa)