produtos = [
    {'nome': 'a', 'preco' : 20,},
    {'nome': 'b', 'preco' : 30,},
    {'nome': 'c', 'preco' : 40,},
]

novos_produtos = [
    {**produto, 'preco' : produto['preco'] * 1.05}
    if produto['preco'] > 30 else {**produto}
    for produto in produtos
]

print(novos_produtos)