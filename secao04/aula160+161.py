import copy

print('='*10, 'QUESTÃO 01', '=' * 10)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# questão 01
novos_produtos = copy.deepcopy(produtos)
 
novos_produtos = [
    {**i, 'preco' : round(i['preco'] * 1.1, 2)}
        for i in produtos
    ]

print(novos_produtos)

# questão 02
print('='*10, 'QUESTÃO 02', '=' * 10)

def ordernar_dic_nome(dic):
    return dic['nome']

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome.sort(key= lambda n: n['nome'], reverse=True)
print(produtos_ordenados_por_nome)


# questão 03
print('='*10, 'QUESTÃO 03', '=' * 10)

def ordernar_dic_preco(dic):
    return dic['preco']

produtos_ordenados_por_preco = copy.deepcopy(produtos)
# produtos_ordenados_por_preco.sort(key = ordernar_dic_preco)
produtos_ordenados_por_preco.sort(key = lambda n: n['preco'])

print(produtos_ordenados_por_preco)