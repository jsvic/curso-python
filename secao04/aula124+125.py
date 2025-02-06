perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
erros = 0

for dic in perguntas:
    print(dic['Pergunta'])
    
    for op in dic['Opções']:
        print(f'{dic['Opções'].index(op)}) {op}')
    resposta = int(input(f'Escolha uma opção: '))

    if dic['Opções'][resposta] == dic['Resposta'] :
        print('Acertou')
        acertos += 1
    else:
        print('Errou')
        erros += 1

print(f'Acertos: {acertos}\nErros : {erros}')