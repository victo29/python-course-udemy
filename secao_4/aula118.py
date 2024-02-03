# Problemas dos parâmetros mutaveis em funções python

def adiciona_clientes(nome,lista=None):
    if lista == None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Adilson')
adiciona_clientes('Aninha', cliente1) #Passando cliente1 como argumento pois na primeira chamada foi criada a lista
cliente1.append('Victor')
print(cliente1)

cliente2 = adiciona_clientes('Iasmin')
adiciona_clientes('Arlete',cliente2)

print(cliente2)