string = 'Victor souza'
quantidade_de_letras = len(string)


contador = 0

while contador < quantidade_de_letras:
    print(string[contador])
    contador+=1
else: #só é executado quando a execução do while for completa
    print('Execução do else')
