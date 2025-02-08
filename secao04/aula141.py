produtos = {
    'nome': 'a',
    'preco' : 3,
    'categoria' : 'a1'
}

novos_produtos = {
    chave: valor * 2
    if isinstance(valor, (int, float)) and valor > 2 else valor
    for chave, valor in produtos.items()
}

print(novos_produtos)

print('=' * 50)

numeros = {
    i ** 2
    for i in range(10)
}

print(numeros)