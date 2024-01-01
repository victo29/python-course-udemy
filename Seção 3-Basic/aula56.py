"""Split e Join coms list e str"""

frase = 'Olha só que interessante, isso é muito louco'

lista_palavras_sem_correcao = frase.split(',') #pode passar algum argumento de referência

lista_palavras_corrigidas = []
for i,frase in enumerate(lista_palavras_sem_correcao):
    lista_palavras_corrigidas.append(lista_palavras_sem_correcao[i].strip())

print(lista_palavras_corrigidas)

palavras_unidas = ', '.join(lista_palavras_corrigidas)
print(palavras_unidas)
