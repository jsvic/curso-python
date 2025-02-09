try:
    a = 18
    b = 0
    c = a / b

    d = a / z

    print('aqui esta um erro'[100000])
except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Variavel não definida')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('Msg: ', error)
    print('Nome: ', error.__class__.__name__)
except Exception:
    print('Erro desconhecido')