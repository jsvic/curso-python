def soma(x, y, z = 0):
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)

# Argumento posicional
soma(1, 2)

# Argumento não posicional (nomeado)
soma(y= 2, x= 1)

# Erro
soma(1, y=2, 3)