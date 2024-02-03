"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, texto):
    return f'{msg}, {texto}!'

def excuta(funcao, *args):
    # return funcao(args[0],args[1])
    return funcao(*args)

# saudacao_2 = saudacao

t = excuta(saudacao, 'Bom dia', 'Victor')
# v = saudacao('Bom dia')
# b = saudacao_2('Bom dia')
# print(v)
print(t)