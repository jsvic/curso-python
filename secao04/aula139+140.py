import pprint 

lista = [
    (x, y)
    for x in range(0, 6)
    for y in range(5, 11)
]

pprint.pprint(lista, sort_dicts= False, width= 30)