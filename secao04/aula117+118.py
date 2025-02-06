def multiplicar(qnt):
    def executar(n):
        return n * qnt
    return executar 

dobro = multiplicar(2)
triplo = multiplicar(3)
quadruplo = multiplicar(4)

print(dobro(10))
print(triplo(10))
print(quadruplo(10))
