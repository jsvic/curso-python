lista = ['Jose', 90, {2,3}, {'altura' : 1.69}, [9, 8, 10]]

for i in lista:
    if isinstance(i, (int, float)):
        print(i * 2)
    elif isinstance(i, str):
        print(i[::-1])
    elif isinstance(i, list):
        print(i[0])
    else:
        print(type(i))