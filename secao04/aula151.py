try:
    print('Sempre executa no inicio')
    c = 9/0
except ZeroDivisionError:
    print('Executa caso tenha algum erro')
else:
    print('Executa caso não tenha erros')
finally:
    print('Sempre executa no final')