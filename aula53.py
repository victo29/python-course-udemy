# enumerate -> enumera iteráveis

lista = ['Victor', 'Iasmin', 'Nelsimara', 'Junior']

lista_enumerada = enumerate(lista)
#print(next(lista_enumerada))
#print(next(lista_enumerada))

#[(0, 'Victor'), (1, 'Iasmin'), (2, 'Nelsimara'), (3, 'Junior')]
lista_enumerada = list(enumerate(lista))#start = number
print(lista_enumerada)


for indice, item in enumerate(lista):
    #a,b = item
    print(indice,item)

