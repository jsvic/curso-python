import copy

pessoa = {
    'nome' : 'José',
    'idade' : 17,
    'altura': 1.69,
    'notas' : [9, 8, 7]
}

print(len(pessoa))
print('='*50)

print(pessoa.keys())
print('='*50)

print(pessoa.values())
print('='*50)

print(pessoa.items())
print('='*50)

print(pessoa.setdefault('peso', 50))
print('='*50)

outra_pessoa1 = pessoa.copy()

print(outra_pessoa1['nome'])

outra_pessoa2 =  outra_pessoa1

outra_pessoa2['nome'] = 'Maria'

print(outra_pessoa1)
print(outra_pessoa2)
print('='*50)

outra_pessoa1['notas'][1] = 6

print(pessoa)
print(outra_pessoa1)
print('='*50)

outra_pessoa3 = copy.deepcopy(pessoa)

outra_pessoa3['notas'] = [10, 9, 10]

print(pessoa)
print(outra_pessoa3)
print('='*50)

print(pessoa.get('carro', 'não possui carro'))
print('='*50)

print(pessoa.pop('peso'))
print(pessoa)
print('='*50)

print(pessoa.popitem())
print(pessoa)
print('='*50)

del pessoa['altura']
print(pessoa)
print('='*50)

pessoa.update(nome='Maria', altura= 1.69)
print(pessoa)