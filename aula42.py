#Qual letra apareceu mais vezes na frase? 

frase = 'O Python é uma linguagem de programação multiparadigma.'\
    'Python foi criado por Guido Van Rossum '


letra_que_mais_apareceu = ''
i = 0
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    if i == 0:
        letra_que_mais_apareceu = letra_atual
    else:
        if frase.count(letra_que_mais_apareceu) < quantas_vezes_letra_apareceu \
            and letra_atual != " ":
            letra_que_mais_apareceu = letra_atual
    i+=1

print("A letra que apareceu mais vezes foi:", letra_que_mais_apareceu)