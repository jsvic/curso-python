def soma1(x, y):
    print(x + y)

def soma2(x, y):
    return x + y

x = soma1(1, 2)
y = soma2(1, 2)

print(x) # valor da soma + None (pois a funcao retorna, por padrao, None)
print(y) # valor da soma