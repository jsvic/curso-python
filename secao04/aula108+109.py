x = 1

global w 
w = 10

def escopo():
    global w
    def outro_escopo():
        z = 3
        print(x)
        print(y)
        print(z)

    y = 2
    w = 12
    print(x)
    print(y)
    # print(z) erro
    outro_escopo()


print(x)
# print(y) erro
# print(z) erro

escopo()
print(w)