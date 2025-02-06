def mensagem(msg):
    return msg

def falar(funcao, msg):
    return funcao(msg)

saudacao = falar(mensagem, 'Bom Dia')

print(saudacao)