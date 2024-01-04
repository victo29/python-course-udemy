"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args):
    #print(args)
    #args = list(args)
    soma = 0
    for i in args:
        soma+=i
    return soma

resultado = soma(1,2,3,4,5,6)
print(resultado)
