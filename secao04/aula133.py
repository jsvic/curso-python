pessoas = [
    {'nome' : 'Jose', 'sobrenome' : 'Silva'},
    {'nome' : 'Carlos', 'sobrenome' : 'Fernando'},
    {'nome' : 'Lucas', 'sobrenome' : 'Ribeiro'}
]

def ordenar_nome(dic):
    return dic['nome']

pessoas.sort(key= ordenar_nome)
print(pessoas)

print('=' * 50)

pessoas.sort(key= lambda item: item['nome'])
print(pessoas)