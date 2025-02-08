lista = ['Jose', 17]
metodo = 'upper'
for i in lista:
    if hasattr(i, metodo):
        print(getattr(i, 'upper')())
    else:
        print(dir(i))