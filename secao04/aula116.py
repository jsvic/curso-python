def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!' 
    return saudar

s1 = criar_saudacao('Bom Dia')
s2 = criar_saudacao('Boa Noite')

print(s1('José'))
print(s2('José'))